import subprocess
import os
import argparse
import sys

class LeanVerifier:
    def __init__(self, project_path):
        self.project_path = os.path.abspath(project_path)
    
        if not os.path.exists(os.path.join(self.project_path, "lakefile.toml")):
            raise FileNotFoundError(f"File lakefile.toml not found under {self.project_path}")

    def verify_file(self, file_path):
        if not os.path.exists(file_path):
            return False, f"File not found: {file_path}"
        
        abs_file_path = os.path.abspath(file_path)

        try:
            try:
                rel_path = os.path.relpath(abs_file_path, self.project_path)
            except ValueError:
                rel_path = abs_file_path

            cmd = ["lake", "env", "lean", rel_path]
            
            result = subprocess.run(
                cmd,
                cwd=self.project_path,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )

            full_output = result.stdout + result.stderr

            if result.returncode != 0 or "error:" in full_output:
                return False, full_output
            else:
                return True, full_output if full_output.strip() else "Check Passed!"

        except Exception as e:
            return False, f"System Error: {str(e)}"

def find_project_root(start_file_path):
    if os.path.isfile(start_file_path):
        current_dir = os.path.dirname(os.path.abspath(start_file_path))
    else:
        current_dir = os.path.abspath(start_file_path)
    
    while True:
        if os.path.exists(os.path.join(current_dir, "lakefile.toml")):
            return current_dir
        
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            return None
        current_dir = parent_dir

# ---------------------------------------------------------
# 以下是命令行入口，保留原功能
# ---------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify a Lean 4 file using Lake.")
    parser.add_argument("lean_file", help="Path to the .lean file to verify")
    parser.add_argument("log_file", help="Path to the output log file")
    
    args = parser.parse_args()
    target_file = args.lean_file
    output_log_path = args.log_file

    project_root = find_project_root(target_file)
    
    content_to_write = ""
    
    if project_root is None:
        content_to_write = f"Error: Could not find 'lakefile.toml' searching up from {target_file}."
        print("Error: Not a valid Lean project.")
    else:
        try:
            verifier = LeanVerifier(project_root)
            success, msg = verifier.verify_file(target_file)
            
            status = 'Accepted' if success else 'Failed'
            content_to_write += f"Lean Verify Result: {status}\n\n"
            content_to_write += "============= Msg =============\n\n"
            content_to_write += msg.strip() + "\n\n"
            content_to_write += "============= Msg =============\n"
            
            print(f"Verification finished. Status: {status}")
            
        except Exception as e:
            content_to_write = f"Script Execution Error: {str(e)}"
            print(f"Script execution error: {e}")

    # 写入日志
    try:
        output_dir = os.path.dirname(os.path.abspath(output_log_path))
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_log_path, "w", encoding="utf-8") as f:
            f.write(content_to_write)
    except Exception as e:
        print(f"Failed to write log file: {e}")