import os
import json
from typing import Optional
import httpx  # 1. 导入 httpx
from openai import OpenAI, APIStatusError  # 2. 导入 APIStatusError
from structure_def.node_def import Structure
from checker.json_structure_checker import JsonStructureChecker

class StructureExtractor:
    def __init__(self, api_key: str, base_url: str, model: str, max_retries: int = 3):
        
        # 3. 定义一个更长的超时时间（例如：120秒）
        #    这能确保我们的客户端比网关更有耐心
        default_timeout = httpx.Timeout(120.0, connect=10.0)
        
        # 4. 将超时配置传递给 OpenAI 客户端
        self.client = OpenAI(
            api_key=api_key, 
            base_url=base_url,
            timeout=default_timeout,
            http_client=httpx.Client(
                timeout=default_timeout
            )
        )
        self.model = model
        self.validator = JsonStructureChecker()
        self.max_retries = max_retries

    def load_prompt_template(self, filepath: str) -> str:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def extract(self, user_text: str, system_prompt_path: str) -> Optional[Structure]:
        system_prompt = self.load_prompt_template(system_prompt_path)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        user_prompt_path = os.path.join(current_dir, "..", "prompts", "structure_extractor_prompt.md")
        user_prompt_template = self.load_prompt_template(user_prompt_path)
        
        json_format = self.validator.get_json_schema()
        
        user_prompt = user_prompt_template.replace("{Json_Format}", json_format)
        user_prompt = user_prompt.replace("{Task_Input}", user_text)
        
        retry_count = 0
        
        while retry_count <= self.max_retries:
            print(f"[Agent: StructurePlanner-structure_extractor] Calling LLM API (model: {self.model}, attempt {retry_count + 1}/{self.max_retries + 1})...")
            
            try:
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.0,
                    response_format={"type": "json_object"},
                )
                response_text = completion.choices[0].message.content
                print("[Agent: StructurePlanner-structure_extractor] LLM responded")
                print(f"response_text: \n {response_text}\n\n")
                
                validated_structure = self.validator.validate_json(response_text)
                
                if validated_structure is not None:
                    print(f"[Agent: StructurePlanner-structure_extractor] JSON validation succeeded on attempt {retry_count + 1}")
                    return validated_structure
                else:
                    # (处理 JSON 验证失败的逻辑...)
                    retry_count += 1
                    if retry_count <= self.max_retries:
                        print(f"[Agent: StructurePlanner-structure_extractor] JSON validation failed, retrying... ({retry_count}/{self.max_retries})")
                    else:
                        print(f"[Agent: StructurePlanner-structure_extractor] JSON validation failed after {self.max_retries + 1} attempts")
                        raise Exception(f"Failed to get valid JSON structure after {self.max_retries + 1} attempts")

            # 5. 添加了专门的 APIStatusError 捕获
            except APIStatusError as e:
                print(f"[Agent: StructurePlanner-structure_extractor] API call failed with status code: {e.status_code}")
                
                print("--- START: Full Error Response Headers ---")
                try:
                    for header, value in e.response.headers.items():
                        print(f"{header}: {value}")
                except Exception as he:
                    print(f"Could not print headers: {he}")
                print("--- END: Full Error Response Headers ---")

                print("--- START: Full Error Response Body ---")
                try:
                    error_data = e.response.json()
                    print(json.dumps(error_data, indent=2))
                except json.JSONDecodeError:
                    print(f"Raw body: {e.response.text}")
                print("--- END: Full Error Response Body ---")

                retry_count += 1
                if retry_count <= self.max_retries:
                    print(f"Retrying... ({retry_count}/{self.max_retries})")
                else:
                    print(f"\n--- ERROR: Failed after {self.max_retries + 1} attempts. ---")
                    return None

            except Exception as e:
                # 6. 其他错误 (例如连接超时)
                retry_count += 1
                if retry_count <= self.max_retries:
                    print(f"[Agent: StructurePlanner-structure_extractor] A non-API error occurred: {e}, retrying... ({retry_count}/{self.max_retries})")
                else:
                    print(f"\n--- ERROR: Failed after {self.max_retries + 1} attempts: {e} ---")
                    return None
        
        return None