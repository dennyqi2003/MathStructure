import subprocess
import os

class LeanVerifier:
    def __init__(self, project_path):
        self.project_path = os.path.abspath(project_path)
        
        if not os.path.exists(os.path.join(self.project_path, "lakefile.toml")):
            raise FileNotFoundError(f"lakefile.toml not found in {self.project_path}")

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