# management/utils.py (MODIFIED)

import json
from pathlib import Path
from typing import Any, Dict, List

# --- Configuration Constants ---
DATASET_FILE = "data_test.json"
WORKSPACE_DIR = "workspace"

SOURCE_MD_FILE = "informal.md" 
STRUCTURE_JSON_FILE = "structure.json"
METADATA_JSON_FILE = "info.json"
LEAN_SKETCH_MD_FILE = "lean_sketch.md"


def get_proof_path(domain: str, proof_id_num: str) -> Path:
    """
    Constructs the standard directory path for a given proof.
    e.g., workspace/Set_Theory/1
    """
    path = Path(WORKSPACE_DIR) / domain / proof_id_num
    path.mkdir(parents=True, exist_ok=True)
    return path


def ask_for_confirmation(prompt: str) -> bool:
    """
    Displays a prompt to the user and asks for a yes/no confirmation.
    """
    while True:
        response = input(f"{prompt} (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")