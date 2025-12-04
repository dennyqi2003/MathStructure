import json
import os

input_file = "input.json"
filename_root, filename_ext = os.path.splitext(input_file)
output_file = f"{filename_root}_index{filename_ext}"

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

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    counter_container = [1]
    processed_data = add_ids_recursive(data, counter_container)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()