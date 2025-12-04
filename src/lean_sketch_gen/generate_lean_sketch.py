import os
import sys
import shutil
import time
from dotenv import load_dotenv
from openai import OpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.add_index import add_index_to_json
from src.lean_sketch_gen.check_coverage import get_next_cursor
from src.lean_sketch_gen.sketch_revise import run_revise_loop, extract_code_block
from src.lean_sketch_gen.logger import LLMQueryLogger

load_dotenv()

DEBUG = os.getenv("DEBUG", "true").lower() == "true"
MAX_SKETCH_GEN_ITER = int(os.getenv("MAX_SKETCH_GEN_ITER"))

GEN_MODEL = os.getenv("SKETCH_GEN_MODEL")
GEN_API_KEY = os.getenv("SKETCH_GEN_API_KEY")
GEN_BASE_URL = os.getenv("SKETCH_GEN_BASE_URL")
GEN_TEMP = float(os.getenv("SKETCH_GEN_TEMP"))

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEAN_PROJECT_ROOT = os.getenv("LEAN_PROJECT_ROOT")
LEAN_SOURCE_DIR = os.getenv("LEAN_SOURCE_DIR", "LeanProject") 

DISPLAY_DIR = os.path.join(PROJECT_ROOT, "display")
LEAN_WORK_DIR = os.path.join(LEAN_PROJECT_ROOT, LEAN_SOURCE_DIR)

gen_client = OpenAI(api_key=GEN_API_KEY, base_url=GEN_BASE_URL)

def call_gen_llm(json_content, current_sketch, cursor):
    prompt_path = os.path.join(PROJECT_ROOT, "prompts", "structure_to_lean_sketch_single_round_prompt.md")
    
    if os.path.exists(prompt_path):
        with open(prompt_path, 'r', encoding='utf-8') as f:
            template = f.read()
    else:
        print(f"Warning: Prompt not found at {prompt_path}")
        return "", ""

    prompt = template.replace("{Structure_Input}", json_content)
    prompt = prompt.replace("{Previous_Sketch_Input}", current_sketch if current_sketch else "")
    prompt = prompt.replace("{Cursor_Input}", str(cursor)) 
    
    try:
        resp = gen_client.chat.completions.create(
            model=GEN_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=GEN_TEMP
        )
        return resp.choices[0].message.content, prompt
    except Exception as e:
        print(f"Gen LLM Error: {e}")
        return "", prompt

def main():
    print(f"Starting Lean Sketch Generation...")
    print(f"Configs: DEBUG={DEBUG}, Max_Gen_Iter={MAX_SKETCH_GEN_ITER}")
    print(f"Project Root: {PROJECT_ROOT}")
    
    os.makedirs(DISPLAY_DIR, exist_ok=True)
    if not os.path.exists(LEAN_WORK_DIR):
        print(f"Error: Lean work dir not found: {LEAN_WORK_DIR}")
        return

    logger = LLMQueryLogger(PROJECT_ROOT, debug_mode=DEBUG)

    structure_json = os.path.join(DISPLAY_DIR, "structure.json")
    structure_index_json = os.path.join(DISPLAY_DIR, "structure_index.json")
    
    backend_temp = os.path.join(LEAN_WORK_DIR, "_temp_gen.lean")
    backend_accumulated = os.path.join(LEAN_WORK_DIR, "_accumulated.lean")
    
    display_temp = os.path.join(DISPLAY_DIR, "llm_output.lean")
    display_accumulated = os.path.join(DISPLAY_DIR, "llm_output_save.lean")
    display_final = os.path.join(DISPLAY_DIR, "lean_sketch.lean")
    display_msg = os.path.join(DISPLAY_DIR, "lean_msg.md")

    print("- Adding index to structure...")
    if not add_index_to_json(structure_json, structure_index_json):
        return

    with open(structure_index_json, 'r', encoding='utf-8') as f:
        json_content_str = f.read()

    open(backend_accumulated, 'w').close()
    open(display_accumulated, 'w').close()
    
    for i in range(1, MAX_SKETCH_GEN_ITER + 1):
        print(f"\nOuter Loop {i}/{MAX_SKETCH_GEN_ITER}")
        
        with open(backend_accumulated, 'r', encoding='utf-8') as f:
            current_code = f.read()
            
        cursor = get_next_cursor(structure_index_json, current_code)
        
        if cursor is None:
            print("All nodes covered! Generation Complete.")
            break
            
        print(f"Cursor: {cursor}")
        
        start_t = time.time()
        raw_resp, used_prompt = call_gen_llm(json_content_str, current_code, cursor)
        logger.log_query("Generate", cursor, GEN_MODEL, used_prompt, raw_resp, start_t)
        
        new_code_candidate = extract_code_block(raw_resp)
        if not new_code_candidate:
            print("No code block found in Gen response.")
            continue
            
        with open(backend_temp, 'w', encoding='utf-8') as f:
            f.write(new_code_candidate)
        with open(display_temp, 'w', encoding='utf-8') as f:
            f.write(new_code_candidate)
            
        print("Verifying and Revising...")
        success, _ = run_revise_loop(
            backend_temp, display_temp, display_msg,
            LEAN_PROJECT_ROOT, logger, cursor
        )
        
        if success:
            print("Step Succeeded.")
            with open(backend_temp, 'r', encoding='utf-8') as f:
                valid_code = f.read()
            
            with open(backend_accumulated, 'w', encoding='utf-8') as f:
                f.write(valid_code)
            with open(display_accumulated, 'w', encoding='utf-8') as f:
                f.write(valid_code)
        else:
            print("Step Failed. Stopping.")
            break

    if os.path.exists(display_accumulated):
        shutil.copy(display_accumulated, display_final)
        print(f"\nFinal Sketch saved to: {display_final}")

if __name__ == "__main__":
    main()