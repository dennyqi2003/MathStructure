import json
import re
from pathlib import Path

# --- 配置 ---

# 目标目录：Path('.') 表示当前脚本所在的目录
# 您也可以指定一个绝对路径，例如: Path(r'C:\Users\YourName\Documents\MyFolder')
TARGET_DIRECTORY = Path('.') 

# 输出文件名
OUTPUT_FILE = 'data.json'

# --- 配置结束 ---

def process_markdown_files(directory_path, output_file):
    """
    扫描目录中的md文件并将其处理为 data.json
    """
    
    # 正则表达式来匹配 'stringNNN.md'
    # 组1 (domain): (.+?)   - 匹配文件名中数字前面的所有字符（非贪婪）
    # 组2 (id):     (\d+)     - 匹配文件名末尾的一个或多个数字
    #           \.md$     - 确保文件以 .md 结尾
    file_pattern = re.compile(r'^(?P<domain>.+?)(?P<id>\d+)\.md$')
    
    all_data = []
    print(f"🚀 开始扫描目录: {directory_path.resolve()}")

    # 遍历目标目录下的所有 .md 文件
    for file_path in directory_path.glob('*.md'):
        filename = file_path.name
        
        # 检查文件名是否符合 'stringNNN.md' 格式
        match = file_pattern.match(filename)
        
        if match:
            try:
                # 从匹配中提取 'domain' 和 'id'
                domain = match.group('domain')
                id_num = int(match.group('id')) # 将ID转换为整数
                
                # 读取文件内容
                # 使用 utf-8 编码确保能正确处理中文字符
                with file_path.open('r', encoding='utf-8') as f:
                    content = f.read()
                
                # 构建符合要求的字典
                file_data = {
                    "id": id_num,
                    "domain": domain,
                    "informal": content,
                    "structure": []
                }
                
                # 添加到总列表中
                all_data.append(file_data)
                print(f"  [✓] 处理成功: {filename} (ID: {id_num}, Domain: {domain})")
                
            except Exception as e:
                print(f"  [✗] 处理 {filename} 时出错: {e}")
        else:
            print(f"  [i] 跳过 (格式不匹配): {filename}")

    # (可选) 建议按 id 对结果进行排序，使json文件更有序
    all_data.sort(key=lambda item: item['id'])

    # 将所有数据写入
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # indent=4 格式化输出 (使其美观)
            # ensure_ascii=False 以便在json中正确显示中文
            json.dump(all_data, f, indent=4, ensure_ascii=False)
        
        print("-" * 30)
        print(f"🎉 处理完成！")
        print(f"总共处理了 {len(all_data)} 个文件。")
        print(f"结果已保存到: {output_file}")
        
    except Exception as e:
        print(f"\n[✗] 写入 {output_file} 失败: {e}")

# --- 运行脚本 ---
if __name__ == "__main__":
    process_markdown_files(TARGET_DIRECTORY, OUTPUT_FILE)