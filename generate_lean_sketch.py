import os
import sys
import shutil
import argparse
import time
from dotenv import load_dotenv
from openai import OpenAI

# 导入我们的辅助模块
from check_coverage import get_next_cursor
from sketch_revise import run_auto_fix, extract_code_block

# 加载环境变量
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 配置参数
MAX_OUTER_LOOPS = 15  # 最大外部生成迭代次数
GEN_PROMPT_PATH = "prompts/structure_to_lean_sketch_single_round_prompt.md"
WORKING_DIR = "lean_project/LeanProject"
TEMP_OUTPUT_FILE = "llm_output.lean"   # LLM 生成的临时文件 (用于 revise)
SAVE_FILE = "llm_save.lean"            # 通过检查的累积文件
LOG_DIR = "logs_sketch"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def read_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def call_gen_llm(json_content, previous_sketch, cursor):
    """
    调用大模型生成下一步的 Sketch
    """
    print(f"\n[Gen] Calling LLM to extend sketch at Cursor {cursor}...")
    
    prompt_template = read_file(GEN_PROMPT_PATH)
    if not prompt_template:
        print(f"Error: Prompt template not found at {GEN_PROMPT_PATH}")
        sys.exit(1)

    # 替换 Prompt 中的占位符
    prompt = prompt_template.replace("{Structure_Input}", json_content)
    
    if not previous_sketch.strip():
        previous_sketch_input = "" # Empty for Cursor 1
    else:
        previous_sketch_input = previous_sketch

    prompt = prompt.replace("{Previous_Sketch_Input}", previous_sketch_input)
    prompt = prompt.replace("{Cursor_Input}", str(cursor))

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return ""

def main():
    parser = argparse.ArgumentParser(description="Iteratively generate Lean sketch from JSON structure.")
    parser.add_argument("json_path", help="Path to the JSON structure file")
    parser.add_argument("output_lean_path", help="Final output path for the Lean file")
    
    args = parser.parse_args()
    
    json_path = args.json_path
    final_output_path = args.output_lean_path

    # 1. 初始化路径
    ensure_dir(LOG_DIR)
    
    llm_save_path = os.path.join(WORKING_DIR, SAVE_FILE)
    llm_output_path = os.path.join(WORKING_DIR, TEMP_OUTPUT_FILE)
    revise_log_path = os.path.join(LOG_DIR, "latest_revise_error.md")

    # 2. 清空 llm_save.lean (初始化)
    print(f"Initializing {llm_save_path}...")
    ensure_dir(os.path.dirname(llm_save_path))
    write_file(llm_save_path, "") 

    # 读取 JSON 内容
    json_content = read_file(json_path)
    if not json_content:
        print(f"Error: JSON file empty or not found at {json_path}")
        sys.exit(1)

    # ================= 主迭代循环 =================
    for iteration in range(1, MAX_OUTER_LOOPS + 1):
        print(f"\n========================================")
        print(f"  Outer Loop Iteration {iteration}/{MAX_OUTER_LOOPS}")
        print(f"========================================")

        # 3. 读取当前已有的 Sketch
        current_sketch = read_file(llm_save_path)
        
        # 4. 计算 Cursor
        cursor = get_next_cursor(json_path, current_sketch)
        
        if cursor is None:
            print(f"🎉 Generation Complete! All JSON IDs covered.")
            break
        
        print(f"ℹ️ Current Cursor: {cursor}")

        # 5. 调用 LLM 生成/续写
        llm_raw_resp = call_gen_llm(json_content, current_sketch, cursor)
        if not llm_raw_resp:
            print("Error: LLM returned empty response. Stopping.")
            break

        new_sketch_code = extract_code_block(llm_raw_resp)
        if not new_sketch_code:
            print("Warning: No code block found in LLM response.")
            new_sketch_code = llm_raw_resp

        # 将生成的代码写入 llm_output.lean 供 sketch_revise 检查
        write_file(llm_output_path, new_sketch_code)
        
        # 保存原始生成代码 log
        log_gen_path = os.path.join(LOG_DIR, f"iter_{iteration}_cursor_{cursor}_gen_raw.lean")
        write_file(log_gen_path, new_sketch_code)

        # 6. 调用 sketch_revise 进行检查和自动修复
        print(f"[Process] Verifying and Revising...")
        revise_success = run_auto_fix(llm_output_path, revise_log_path)

        if not revise_success:
            print(f"❌ Iteration {iteration} Failed: Revision could not fix the code.")
            print("Stopping iteration.")
            break
        
        print(f"✅ Iteration {iteration} Success: Code verified and saved.")
        
        # 读取刚刚保存的 llm_save.lean 进行日志记录
        saved_code = read_file(llm_save_path)
        log_save_path = os.path.join(LOG_DIR, f"iter_{iteration}_cursor_{cursor}_verified.lean")
        write_file(log_save_path, saved_code)

    # ================= 结束处理 =================
    print(f"\n========================================")
    
    if os.path.exists(llm_save_path):
        print(f"Copying result to final output: {final_output_path}")
        shutil.copy2(llm_save_path, final_output_path)
    else:
        print("Error: No result file generated.")

if __name__ == "__main__":
    main()