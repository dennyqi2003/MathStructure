import os
import time
from datetime import datetime

class LLMQueryLogger:
    def __init__(self, project_root, debug_mode=True):
        self.debug_mode = debug_mode
        if not self.debug_mode:
            return

        self.log_dir = os.path.join(project_root, "display", "llm_query_log_sketch_gen")
        os.makedirs(self.log_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(self.log_dir, f"log_{timestamp}.log")
        print(f"LLM Query Log (Debug={debug_mode}): {self.log_file}")

    def log_query(self, step, cursor, model, prompt, response, start_time):
        if not self.debug_mode:
            return

        end_time = time.time()
        latency = end_time - start_time
        timestamp_str = datetime.now().isoformat()
        
        log_entry = (
            f"\n{'='*80}\n"
            f"[{timestamp_str}] Step: {step} | Cursor: {cursor} | Model: {model} | Latency: {latency:.2f}s\n"
            f"{'='*80}\n\n"
            f">>> INPUT PROMPT >>>\n"
            f"{prompt}\n"
            f"<<< END INPUT <<<\n\n"
            f">>> OUTPUT RESPONSE >>>\n"
            f"{response}\n"
            f"<<< END OUTPUT <<<\n"
            f"{'-'*80}\n"
        )
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Failed to write log: {e}")