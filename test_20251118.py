#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script automates the processing of chapter markdown files.

It iterates through numbered chapter directories (1 to 20) and performs the
following steps for each:
1. Copies 'informal.md' from the chapter folder to the root directory.
2. Runs the 'get_structure_with_revise_iteration.py' script.
3. Copies the resulting 'result.json' from the root directory back to the
   chapter folder as 'structure.json'.
4. Cleans up the root directory files.
"""

import os
import shutil
import subprocess
import sys

# --- Configuration ---

# The base path where all the numbered chapter folders are located
BASE_DATA_DIR = "data/workspace/Analysis"

# The name of the Python script to run in the root directory
SCRIPT_TO_RUN = "get_structure_with_revise_iteration.py"

# The name of the source markdown file in each chapter folder
SOURCE_MD_FILENAME = "informal.md"

# The name of the target structure file in each chapter folder
TARGET_JSON_FILENAME = "structure.json"

# The temporary file names in the root directory
ROOT_MD_PATH = "informal.md"
ROOT_JSON_PATH = "result.json"

# The range of chapter numbers to process
START_CHAPTER = 148
END_CHAPTER = 158

# --- End of Configuration ---


def main():
    """
    Main function to run the batch processing.
    """
    print("Starting batch processing...")

    # Use sys.executable to ensure we use the same Python interpreter
    # that is running this script.
    python_executable = sys.executable

    # Check if the main script to run exists
    if not os.path.exists(SCRIPT_TO_RUN):
        print(f"Error: The script '{SCRIPT_TO_RUN}' was not found.")
        print("Please make sure it is in the same directory as this script.")
        return

    try:
        # Loop from START_CHAPTER to END_CHAPTER (inclusive)
        for i in range(START_CHAPTER, END_CHAPTER + 1):
            
            # Convert the chapter number to a string
            chapter_num_str = str(i)
            print(f"\n--- Processing Chapter {chapter_num_str} ---")

            # 1. Define paths for the current chapter
            
            # e.g., "data/workspace/Abstract_Algebra/1"
            chapter_dir = os.path.join(BASE_DATA_DIR, chapter_num_str)
            
            # e.g., "data/workspace/Abstract_Algebra/1/informal.md"
            source_md_path = os.path.join(chapter_dir, SOURCE_MD_FILENAME)
            
            # e.g., "data/workspace/Abstract_Algebra/1/structure.json"
            target_json_path = os.path.join(chapter_dir, TARGET_JSON_FILENAME)

            # Check if the source file exists
            if not os.path.exists(source_md_path):
                print(f"Warning: Source file not found, skipping chapter {chapter_num_str}.")
                print(f"Missing file: {source_md_path}")
                continue  # Go to the next chapter

            # 2. Copy the chapter's .md file to the root directory
            try:
                print(f"Copying {source_md_path} to {ROOT_MD_PATH}...")
                shutil.copy(source_md_path, ROOT_MD_PATH)
            except Exception as e:
                print(f"Error copying {source_md_path}: {e}")
                continue # Skip to the next chapter

            # 3. Run the external Python script
            print(f"Running {SCRIPT_TO_RUN}...")
            print("--- (Output from external script starts) ---")
            
            try:
                # *** THIS IS THE CHANGED PART ***
                # We removed 'capture_output=True' and 'text=True'.
                # The output from SCRIPT_TO_RUN will now stream to
                # the console in real-time, just as you wanted.
                subprocess.run(
                    [python_executable, SCRIPT_TO_RUN], 
                    check=True  # 'check=True' will raise an exception if the script fails
                )
                
                # The 'print' statements from the script will appear *before* this line
                print("--- (Output from external script ends) ---")
                print("Script finished successfully.")
                
            except subprocess.CalledProcessError as e:
                # The error message from the script will have already
                # been printed to the console.
                print("--- (Output from external script ends) ---")
                print(f"\nError: The script {SCRIPT_TO_RUN} failed for chapter {chapter_num_str}.")
                print(f"Return Code: {e.returncode}")
                print("Please check the error message above.")
                print("Stopping the process.")
                break  # Exit the loop entirely if the script fails
            except Exception as e:
                # This catches other errors, like not finding the script
                print(f"An unexpected error occurred while running the script: {e}")
                break # Exit the loop

            # 4. Check if the result.json file was created
            if not os.path.exists(ROOT_JSON_PATH):
                print(f"Error: {SCRIPT_TO_RUN} did not create {ROOT_JSON_PATH}.")
                print(f"Skipping copy for chapter {chapter_num_str}.")
                continue # Go to the next chapter

            # 5. Copy the generated result.json to the chapter's directory
            try:
                print(f"Copying {ROOT_JSON_PATH} to {target_json_path}...")
                shutil.copy(ROOT_JSON_PATH, target_json_path)
            except Exception as e:
                print(f"Error copying {ROOT_JSON_PATH} to {target_json_path}: {e}")
                # Continue to the next chapter even if copy fails
                continue

    finally:
        # --- Cleanup ---
        # This 'finally' block will run whether the script finishes
        # or encounters an error, ensuring temporary files are removed.
        print("\n--- Cleaning up temporary files ---")
        
        if os.path.exists(ROOT_MD_PATH):
            try:
                os.remove(ROOT_MD_PATH)
                print(f"Removed {ROOT_MD_PATH}.")
            except Exception as e:
                print(f"Error removing {ROOT_MD_PATH}: {e}")

        if os.path.exists(ROOT_JSON_PATH):
            try:
                os.remove(ROOT_JSON_PATH)
                print(f"Removed {ROOT_JSON_PATH}.")
            except Exception as e:
                print(f"Error removing {ROOT_JSON_PATH}: {e}")

    print("\nBatch processing complete.")


# This ensures that the main() function is called when the script is run directly
if __name__ == "__main__":
    main()