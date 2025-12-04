import os
import json
import time
import sys
from openai import OpenAI
from dotenv import load_dotenv
from .node_def import Structure

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils.json_utils import extract_json_from_markdown

load_dotenv()

MODEL = os.getenv("STRUCTURE_REVISE_MODEL")
API_KEY = os.getenv("STRUCTURE_REVISE_API_KEY")
BASE_URL = os.getenv("STRUCTURE_REVISE_BASE_URL")
TEMPERATURE = float(os.getenv("STRUCTURE_REVISE_TEMP"))

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

class StructureReviser:
    def __init__(self, logger=None):
        self.logger = logger
        self.model = MODEL

    def revise(self, natural_language: str, current_json: str, eval_json: str, project_root: str, iteration: int) -> str:
        prompts_dir = os.path.join(project_root, "prompts")
        guide_path = os.path.join(prompts_dir, "structure_system_prompt.md")
        revise_path = os.path.join(prompts_dir, "revise_prompt.md")
        
        with open(guide_path, 'r', encoding='utf-8') as f: sys_prompt = f.read()
        with open(revise_path, 'r', encoding='utf-8') as f: template = f.read()
        
        user_prompt = template.replace("{Natural_Language_Text}", natural_language)
        user_prompt = user_prompt.replace("{Json_Structure_to_Revise}", current_json)
        user_prompt = user_prompt.replace("{Evaluation_Structure}", eval_json)
        
        start_time = time.time()
        try:
            resp = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=TEMPERATURE,
                response_format={"type": "json_object"}
            )
            raw_content = resp.choices[0].message.content
            
            cleaned_content = extract_json_from_markdown(raw_content)
            
            if self.logger:
                full_log_input = f"--- [SYSTEM PROMPT] ---\n{sys_prompt}\n\n--- [USER PROMPT] ---\n{user_prompt}"
                self.logger.log_query("Revision", iteration, self.model, full_log_input, raw_content, start_time)
            
            Structure.model_validate_json(cleaned_content)
            return cleaned_content
            
        except Exception as e:
            print(f"Revision Error: {e}")
            return ""