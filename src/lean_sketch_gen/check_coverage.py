import json
import re
import os

def extract_ids_from_json(data):
    ids = set()
    if isinstance(data, dict):
        if 'id' in data:
            try:
                ids.add(int(data['id']))
            except (ValueError, TypeError):
                pass
        for value in data.values():
            ids.update(extract_ids_from_json(value))
    elif isinstance(data, list):
        for item in data:
            ids.update(extract_ids_from_json(item))
    return ids

def extract_ids_from_lean(file_content):
    pattern = r'--\s*\[(\d+)\]'
    matches = re.findall(pattern, file_content)
    return set(map(int, matches))

def get_next_cursor(json_path, lean_content):
    if not os.path.exists(json_path):
        print(f"Error: JSON index file not found: {json_path}")
        return None

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return None

    expected_ids = extract_ids_from_json(json_data)
    found_ids = extract_ids_from_lean(lean_content)
    
    missing_ids = expected_ids - found_ids
    
    if not missing_ids:
        return None
    
    return min(missing_ids)