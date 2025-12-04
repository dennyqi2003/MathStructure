import sys
import os

def add_line_numbers(input_path, output_path):
    # 1. 检查输入文件是否存在
    if not os.path.exists(input_path):
        print(f"❌ 错误：找不到文件 '{input_path}'")
        return

    try:
        # 2. 读取文件
        with open(input_path, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        total_lines = len(lines)
        width = len(str(total_lines)) # 计算行号宽度用于对齐

        # 3. 写入文件
        with open(output_path, 'w', encoding='utf-8') as f_out:
            for index, line in enumerate(lines, start=1):
                # 格式化：行号右对齐 | 内容
                f_out.write(f"{index:>{width}} | {line}")

        print(f"✅ 处理完成！")
        print(f"📄 输入: {input_path}")
        print(f"📄 输出: {output_path} (共 {total_lines} 行)")

    except Exception as e:
        print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    # sys.argv[0] 是脚本本身的名字
    # sys.argv[1] 是第一个参数 (输入文件)
    # sys.argv[2] 是第二个参数 (输出文件)

    # 检查参数数量是否正确
    if len(sys.argv) != 3:
        print("⚠️ 使用方法错误。请按照以下格式运行：")
        print(f"python {sys.argv[0]} <输入文件路径> <输出文件路径>")
        print("示例: python add_lines.py input.txt output.txt")
    else:
        # 获取参数并执行
        in_file = sys.argv[1]
        out_file = sys.argv[2]
        add_line_numbers(in_file, out_file)