import json
import os

def add_ids_recursive(data, counter_container):
    if isinstance(data, list):
        return [add_ids_recursive(item, counter_container) for item in data]
    if isinstance(data, dict):
        new_dict = {}
        if "type" in data:
            new_dict["id"] = counter_container[0]
            counter_container[0] += 1

        for key, value in data.items():
            new_dict[key] = add_ids_recursive(value, counter_container)
        
        return new_dict
    return data

def add_index_to_json(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: Input JSON not found: {input_path}")
        return False

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        counter_container = [1]
        processed_data = add_ids_recursive(data, counter_container)
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
        
        print(f"Indexed JSON saved to: {output_path}")
        return True
    except Exception as e:
        print(f"Error adding index: {e}")
        return False