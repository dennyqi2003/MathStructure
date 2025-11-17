import json
import os

# --- 1. 定义文件名 ---

# !! 重要：请在这里设置你要读取的文件名 !!
# 
# 假设你删除条目后的文件是 'data_sorted_reordered.json'。
# 如果你把它重命名了（比如 'my_edited_data.json'），请在下面更改它。
INPUT_FILE = 'data_test_proofnet.json'

# 这是重新编号后要保存的新文件名
OUTPUT_FILE = 'data_test.json'

def re_index_ids():
    """
    加载一个 JSON 文件，重新将其中的 'id' 字段从 1 开始连续编号，
    然后保存到一个新文件。
    """
    
    # --- 步骤 1: 加载你编辑过的文件 ---
    try:
        # 确保脚本和文件在同一目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_path = os.path.join(script_dir, INPUT_FILE)
        
        with open(input_path, 'r', encoding='utf-8') as f:
            all_proofs = json.load(f)
            
        if not isinstance(all_proofs, list):
            print(f"错误：文件 {INPUT_FILE} 的顶层结构不是一个列表 (list)。")
            return

    except FileNotFoundError:
        print(f"错误：未在脚本目录中找到文件 {INPUT_FILE}。")
        print(f"请确保该文件 '{INPUT_FILE}' 与此脚本在同一目录，")
        print("或者已在脚本中正确设置 INPUT_FILE 变量。")
        return
    except json.JSONDecodeError:
        print(f"错误：文件 {INPUT_FILE} 格式不正确，无法解析JSON。")
        return
    except Exception as e:
        print(f"加载文件时发生未知错误: {e}")
        return

    print(f"成功加载 {len(all_proofs)} 条数据。")

    # --- 步骤 2: 重新编号 ID ---
    
    # 遍历列表，使用 enumerate 来获取从 0 开始的索引 i
    for i, proof in enumerate(all_proofs):
        # 将 'id' 设置为 索引(i) + 1
        proof['id'] = i + 1
    
    print(f"已将 ID 重新编号 (从 1 到 {len(all_proofs)})。")

    # --- 步骤 3: 保存结果到新文件 ---
    try:
        output_path = os.path.join(script_dir, OUTPUT_FILE)
        with open(output_path, 'w', encoding='utf-8') as f:
            # 保持和之前一样的漂亮格式
            json.dump(all_proofs, f, indent=4, ensure_ascii=False)
        
        print(f"处理完成！重新编号后的数据已保存到 {OUTPUT_FILE}")

    except Exception as e:
        print(f"保存文件时发生错误: {e}")

# 运行主函数
if __name__ == "__main__":
    re_index_ids()