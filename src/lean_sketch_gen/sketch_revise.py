import os
import re
import shutil
import time
from openai import OpenAI
from dotenv import load_dotenv

try:
    from utils.line_numbering import add_line_numbers_to_string
    from .lean_verifier import LeanVerifier
except ImportError:
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from utils.line_numbering import add_line_numbers_to_string
    from src.lean_sketch_gen.lean_verifier import LeanVerifier

load_dotenv()

REVISE_MODEL = os.getenv("SKETCH_REVISE_MODEL")
REVISE_API_KEY = os.getenv("SKETCH_REVISE_API_KEY")
REVISE_BASE_URL = os.getenv("SKETCH_REVISE_BASE_URL")
MAX_RETRIES = int(os.getenv("MAX_SKETCH_REVISE_RETRIES"))
REVISE_TEMP = float(os.getenv("SKETCH_REVISE_TEMP"))

client = OpenAI(api_key=REVISE_API_KEY, base_url=REVISE_BASE_URL)

def call_revise_llm(prompt):
    try:
        response = client.chat.completions.create(
            model=REVISE_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=REVISE_TEMP
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling Revise LLM: {e}")
        return ""

def extract_code_block(text):
    pattern = r"```lean(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return matches[0].strip()
    return text.strip()

def run_revise_loop(file_path_backend, file_path_display, log_file_display, lean_root, logger, cursor):
    verifier = LeanVerifier(lean_root)
    
    prompt_path = os.path.join(os.path.dirname(lean_root), "prompts", "sketch_revise_prompt.md")
    if not os.path.exists(prompt_path):
        prompt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "prompts", "sketch_revise_prompt.md"))

    if os.path.exists(prompt_path):
        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt_template = f.read()
    else:
        prompt_template = "Code:\n{Sketch_Input}\n\nError:\n{Compiler_Input}\n\nFix it."

    print(f"Starting Revise Loop (Max {MAX_RETRIES})...")

    for i in range(MAX_RETRIES + 1):
        success, msg = verifier.verify_file(file_path_backend)
        
        display_msg = msg.replace(os.path.basename(file_path_backend), os.path.basename(file_path_display))
        with open(log_file_display, 'w', encoding='utf-8') as f:
            f.write(f"# Compile Result (Iter {i})\n\n```text\n{display_msg}\n```")

        if success:
            print(f"Check Passed at iteration {i}!")
            return True, None

        if i == MAX_RETRIES:
            print("Max retries reached.")
            return False, msg

        print(f"Check Failed (Iter {i}). Revising...")

        with open(file_path_backend, 'r', encoding='utf-8') as f:
            current_code = f.read()
        
        numbered_code = add_line_numbers_to_string(current_code)
        
        prompt = prompt_template.replace("{Sketch_Input}", numbered_code)
        prompt = prompt.replace("{Compiler_Input}", display_msg)
        start_time = time.time()
        response = call_revise_llm(prompt)
        logger.log_query("Revise", cursor, REVISE_MODEL, prompt, response, start_time)

        new_code = extract_code_block(response)
        if not new_code:
            print("Error: Empty code from LLM.")
            continue

        with open(file_path_backend, 'w', encoding='utf-8') as f:
            f.write(new_code)
        with open(file_path_display, 'w', encoding='utf-8') as f:
            f.write(new_code)
            
    return False, msg