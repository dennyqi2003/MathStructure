import os
import sys
import shutil
import argparse
import re
from dotenv import load_dotenv
from openai import OpenAI
from lean_verifier import LeanVerifier, find_project_root

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

# 确保在被导入时也能初始化 client
client = None
if API_KEY:
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
else:
    print("Warning: OPENAI_API_KEY not found in environment variables.")

MAX_RETRIES = 5
PROMPT_TEMPLATE_PATH = "prompts/sketch_revise_prompt.md"

def load_prompt_template(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        print(f"Warning: Prompt template not found at {path}. Using fallback.")
        return ""

def call_llm_api(prompt_content):
    print(f"\n[Sys] Calling LLM ({MODEL_NAME})...")
    
    if not client:
        print("Error: Client not initialized.")
        return ""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user", 
                    "content": prompt_content
                }
            ],
            temperature=0.2, 
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return ""

def extract_code_block(llm_response):
    if not llm_response:
        return ""

    pattern = r"```lean(.*?)```"
    matches = re.findall(pattern, llm_response, re.DOTALL)
    if matches:
        return matches[0].strip()
    
    pattern_generic = r"```(.*?)```"
    matches_generic = re.findall(pattern_generic, llm_response, re.DOTALL)
    if matches_generic:
        return matches_generic[0].strip()
        
    return llm_response.strip()

def save_log(path, success, msg):
    status = 'Accepted' if success else 'Failed'
    content = msg.strip()
    
    try:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing log: {e}")

def run_auto_fix(lean_file_path, log_file_path):
    """
    封装后的主逻辑，供外部调用。
    返回: True (成功/通过验证), False (失败/达到最大重试次数)
    """
    current_lean_file = os.path.abspath(lean_file_path)
    log_file_path = os.path.abspath(log_file_path)
    
    dir_name = os.path.dirname(current_lean_file)
    save_file_path = os.path.join(dir_name, "llm_save.lean")

    project_root = find_project_root(current_lean_file)
    if not project_root:
        print(f"Error: Cannot find lakefile.toml project root for {current_lean_file}")
        return False
        
    verifier = LeanVerifier(project_root)
    prompt_template = load_prompt_template(PROMPT_TEMPLATE_PATH)

    print(f"Starting auto-fix loop for: {current_lean_file}")
    
    for i in range(MAX_RETRIES + 1):
        print(f"\n--- [Revise] Iteration {i} ---")
        
        success, msg = verifier.verify_file(current_lean_file)
        
        if success:
            print("Check Passed!")
            shutil.copy2(current_lean_file, save_file_path)
            print(f"Success! File saved to: {save_file_path}")
            save_log(log_file_path, True, msg)
            return True
        
        print("Check Failed.")
        save_log(log_file_path, False, msg)
        
        if i == MAX_RETRIES:
            print("Maximum retries reached. Fix failed.")
            return False

        print("Preparing Prompt for LLM...")
        
        with open(current_lean_file, 'r', encoding='utf-8') as f:
            current_code = f.read()
            
        # 如果 prompt template 为空，构造一个默认的
        if not prompt_template:
            prompt_content = f"The following Lean code has errors:\n\n```lean\n{current_code}\n```\n\nError Message:\n{msg}\n\nPlease fix it."
        else:
            prompt_content = prompt_template.replace("{Sketch_Input}", current_code)
            prompt_content = prompt_content.replace("{Compiler_Input}", msg)
        
        raw_response = call_llm_api(prompt_content)
        
        if not raw_response:
            print("Error: Empty response from LLM. Retrying might not help but continuing...")
        
        new_code = extract_code_block(raw_response)
        
        if not new_code:
            print("Error: Could not extract code block from LLM response.")
            continue

        with open(current_lean_file, 'w', encoding='utf-8') as f:
            f.write(new_code)
            
        print(f"File updated with LLM response.")
    
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-fix Lean 4 code using LLM iteration.")
    parser.add_argument("lean_file", help="Path to the input .lean file (e.g., llm_output.lean)")
    parser.add_argument("log_file", help="Path to save error logs (e.g., lean_msg.md)")
    
    args = parser.parse_args()
    
    success = run_auto_fix(args.lean_file, args.log_file)
    sys.exit(0 if success else 1)