import os
import time
import sys
from openai import OpenAI
from dotenv import load_dotenv

from .node_def import Structure 
from .evaluation_def import EvaluationResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils.json_utils import extract_json_from_markdown

load_dotenv()

MODEL = os.getenv("STRUCTURE_EVAL_MODEL")
API_KEY = os.getenv("STRUCTURE_EVAL_API_KEY")
BASE_URL = os.getenv("STRUCTURE_EVAL_BASE_URL")
TEMPERATURE = float(os.getenv("STRUCTURE_EVAL_TEMP"))

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

class StructureEvaluator:
    def __init__(self, logger=None):
        self.logger = logger
        self.model = MODEL

    def evaluate(self, natural_language: str, structure_json: str, project_root: str, iteration: int) -> str:
        prompts_dir = os.path.join(project_root, "prompts")
        guide_path = os.path.join(prompts_dir, "structure_system_prompt.md")
        judge_path = os.path.join(prompts_dir, "judge_prompt.md")
        
        with open(guide_path, 'r', encoding='utf-8') as f: guide_prompt = f.read()
        with open(judge_path, 'r', encoding='utf-8') as f: judge_prompt = f.read()
        
        system_prompt = f"{guide_prompt}\n\n---\n\n{judge_prompt}"
        
        try:
            struct_obj = Structure.model_validate_json(structure_json)
            cleaned_structure_json = struct_obj.model_dump_json(indent=2, exclude={"thinking"})
        except Exception as e:
            print(f"Warning: Failed to clean structure JSON for evaluation: {e}")
            cleaned_structure_json = structure_json

        user_prompt = (
            "## Your Task\n\n"
            "**Natural language text:**\n"
            f"\"\"\"\n{natural_language}\n\"\"\"\n\n"
            "**Structure:**\n"
            f"```json\n{cleaned_structure_json}\n```\n\n"
            "**Evaluation:**\n"
        )
        
        start_time = time.time()
        try:
            resp = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=TEMPERATURE,
                response_format={"type": "json_object"}
            )
            raw_content = resp.choices[0].message.content
            
            cleaned_content = extract_json_from_markdown(raw_content)
            
            if self.logger:
                full_log_input = f"--- [SYSTEM PROMPT] ---\n{system_prompt}\n\n--- [USER PROMPT] ---\n{user_prompt}"
                self.logger.log_query("Evaluation", iteration, self.model, full_log_input, raw_content, start_time)
            
            EvaluationResult.model_validate_json(cleaned_content)
            return cleaned_content
            
        except Exception as e:
            print(f"Evaluation Error: {e}")
            return ""