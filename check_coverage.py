import json
import re
import sys
import os

def extract_ids_from_json(data):
    """
    递归遍历 JSON 数据结构，提取所有的 'id' 字段值。
    返回一个包含所有 ID 的集合 (set of integers)。
    """
    ids = set()

    if isinstance(data, dict):
        if 'id' in data:
            try:
                ids.add(int(data['id']))
            except (ValueError, TypeError):
                pass
        
        for key, value in data.items():
            ids.update(extract_ids_from_json(value))
            
    elif isinstance(data, list):
        for item in data:
            ids.update(extract_ids_from_json(item))
            
    return ids

def extract_ids_from_lean(file_content):
    """
    使用正则表达式从 Lean 代码中提取标注的 ID。
    """
    pattern = r'--\s*\[(\d+)\]'
    matches = re.findall(pattern, file_content)
    return set(map(int, matches))

def get_next_cursor(json_path, lean_path_or_content):
    """
    计算下一个 Cursor (即第一个缺失的 ID)。
    如果所有 ID 都已覆盖，返回 None。
    lean_path_or_content 可以是文件路径，也可以是直接的内容字符串。
    """
    # 1. 获取所有 Expected IDs
    if not os.path.exists(json_path):
        print(f"Error: JSON file not found at {json_path}")
        return None

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file. {e}")
        return None

    expected_ids = extract_ids_from_json(json_data)
    
    # 2. 获取 Found IDs
    lean_content = ""
    if os.path.isfile(lean_path_or_content):
        with open(lean_path_or_content, 'r', encoding='utf-8') as f:
            lean_content = f.read()
    else:
        lean_content = lean_path_or_content

    found_ids = extract_ids_from_lean(lean_content)

    # 3. 找出缺失的 IDs
    missing_ids = expected_ids - found_ids
    
    if not missing_ids:
        return None # All covered
    
    # 返回最小的缺失 ID 作为 Cursor
    return min(missing_ids)

def check_termination(json_path, lean_path):
    """
    主逻辑函数 (保留用于兼容性或单独调用)
    """
    cursor = get_next_cursor(json_path, lean_path)
    
    if cursor is None:
        print("✅ TERMINATION CONDITION MET: All IDs are covered.")
        return True
    else:
        print(f"❌ CONTINUE ITERATION: Next Cursor is {cursor}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_coverage.py <json_file_path> <lean_file_path>")
    else:
        json_file = sys.argv[1]
        lean_file = sys.argv[2]
        is_complete = check_termination(json_file, lean_file)
        sys.exit(0 if is_complete else 1)