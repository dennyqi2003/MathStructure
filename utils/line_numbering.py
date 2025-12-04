def add_line_numbers_to_string(code_str):
    lines = code_str.splitlines()
    total_lines = len(lines)
    width = len(str(total_lines))
    
    numbered_lines = []
    for index, line in enumerate(lines, start=1):
        numbered_lines.append(f"{index:>{width}} | {line}")
    
    return "\n".join(numbered_lines)