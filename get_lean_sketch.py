import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

def main():

    # --- 1. Load Configuration ---
    try:
        load_dotenv()
        API_KEY = os.getenv("OPENAI_API_KEY")
        BASE_URL = os.getenv("OPENAI_BASE_URL")
        MODEL_NAME = os.getenv("MODEL_NAME")

        if not all([API_KEY, BASE_URL, MODEL_NAME]):
            print("Error: Environment variables OPENAI_API_KEY, OPENAI_BASE_URL, or MODEL_NAME are not set.")
            print("Please ensure your .env file is in the correct location and contains these values.")
            sys.exit(1)
            
        print("Environment variables loaded successfully.")

    except Exception as e:
        print(f"Error: Failed to load .env file: {e}")
        sys.exit(1)

    # --- 2. Define File Paths ---
    # Use os.path.abspath(__file__) to get the absolute path of the current script
    # Then use os.path.dirname() to get the directory containing the script
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Construct file paths based on your requirements
    PROMPT_TEMPLATE_PATH = os.path.join(CURRENT_DIR, "prompts", "structure_to_lean_sketch_prompt.md")
    JSON_DATA_PATH = os.path.join(CURRENT_DIR, "result.json")
    OUTPUT_FILE_PATH = os.path.join(CURRENT_DIR, "lean_project", "LeanProject", "llm_output.lean")

    print(f"   - Prompt Template: {PROMPT_TEMPLATE_PATH}")
    print(f"   - JSON Data: {JSON_DATA_PATH}")
    print(f"   - Output File: {OUTPUT_FILE_PATH}")

    # --- 3. Read Input Files ---
    try:
        with open(PROMPT_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            prompt_template = f.read()
        print("Prompt template read successfully.")
    except FileNotFoundError:
        print(f"Error: Prompt template file not found: {PROMPT_TEMPLATE_PATH}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Failed to read prompt template: {e}")
        sys.exit(1)

    try:
        with open(JSON_DATA_PATH, 'r', encoding='utf-8') as f:
            json_content = f.read()
        print("result.json data read successfully.")
    except FileNotFoundError:
        print(f"Error: JSON data file not found: {JSON_DATA_PATH}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Failed to read JSON data: {e}")
        sys.exit(1)

    # --- 4. Build Final Prompt ---
    final_prompt = prompt_template.replace("{Json_structure}", json_content)
    
    # Check if replacement was successful
    if "{Json_structure}" in final_prompt:
        print("Warning: Placeholder '{Json_structure}' not found in the prompt template.")
    else:
        print("Final prompt built successfully (JSON injected).")


    # --- 5. Call LLM API ---
    try:
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
        print(f"Calling LLM API (Model: {MODEL_NAME})...")
        
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": final_prompt  # Send the final prompt with all instructions as a single user message
                }
            ],
            temperature=0.0  # Ensure deterministic output
            # Note: We don't use response_format={"type": "json_object"} here because we need raw text output
        )
        
        llm_output = completion.choices[0].message.content
        print("LLM API response successful.")

    except Exception as e:
        print(f"Error: LLM API call failed: {e}")
        sys.exit(1)

    # --- 6. Clean LLM Output (Robustness) ---
    # 检查并移除大模型输出中可能包含的 "```" 代码围栏
    
    print("Cleaning LLM output...")
    
    # 首先，移除开头和结尾的任何空白（包括换行符）
    llm_output = llm_output.strip()
    
    # 将输出分割成行列表
    lines = llm_output.splitlines()
    
    # 检查是否至少有2行，并且第一行以"```"开头，最后一行是"```"
    if len(lines) >= 2 and lines[0].strip().startswith("```") and lines[-1].strip() == "```":
        print("   - Detected code fences (```) on first and last lines. Removing them.")
        # 如果是，则只保留中间的内容（从第二行到倒数第二行）
        llm_output = "\n".join(lines[1:-1])
        # 再次清理，以防中间内容本身前后有多余的换行
        llm_output = llm_output.strip()
    else:
        print("   - Code fences not detected on both first and last lines. No lines removed.")

    print("LLM output cleaned.")

    # --- 7. Write Output File ---
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(OUTPUT_FILE_PATH)
        if output_dir:  # Check if the path is not empty
            os.makedirs(output_dir, exist_ok=True)
            print(f"   - Ensuring directory exists: {output_dir}")
        
        with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(llm_output)
        
        print(f"Success! Lean sketch saved to: {OUTPUT_FILE_PATH}")

    except Exception as e:
        print(f"Error: Failed to write output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()