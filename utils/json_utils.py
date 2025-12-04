import json
from typing import Any, Dict, List, Union
import re

def create_initial_structure_string(natural_language_text: str) -> str:
    initial_data = {
        "thinking": "Initial extraction",
        "structure": [
            {
                "type": "PlaceHolder",
                "text": natural_language_text
            }
        ]
    }
    return json.dumps(initial_data, indent=2, ensure_ascii=False)

def _format_content(content: Any) -> str:
    if isinstance(content, list):
        return "; ".join(str(item) for item in content)
    return str(content)

def pretty_print_structure(json_data: Union[Dict[str, Any], List[Dict[str, Any]], int], indent_level: int = 0) -> str:
    indent = "    " * indent_level
    
    if isinstance(json_data, list):
        result = []
        for item in json_data:
            result.append(pretty_print_structure(item, indent_level))
        return "\n".join(result)
    
    if not isinstance(json_data, dict):
        return f"{indent}{json_data}"
    
    node_type = json_data.get("type", "")
    result_lines = []
    
    if node_type == "Show":
        content = _format_content(json_data.get("proposition", []))
        method = json_data.get("method")
        line = f"{indent}[Show] {{{content}}}"
        if method:
            line += f" using {{{_format_content(method)}}}"
        result_lines.append(line)
        
    elif node_type == "Assume":
        content = _format_content(json_data.get("assumption", []))
        result_lines.append(f"{indent}[Assume] {{{content}}}")
        
    elif node_type == "Fix":
        vars_str = _format_content(json_data.get("variable", []))
        cond = json_data.get("condition")
        line = f"{indent}[Fix] {{{vars_str}}}"
        if cond:
            line += f" such that {{{_format_content(cond)}}}"
        result_lines.append(line)
        
    elif node_type == "Have":
        content = _format_content(json_data.get("claim", []))
        reason = json_data.get("reason")
        line = f"{indent}[Have] {{{content}}}"
        if reason:
            line += f" by {{{_format_content(reason)}}}"
        result_lines.append(line)
        
    elif node_type == "Obtain":
        vars_str = _format_content(json_data.get("obtained_variable", []))
        cond = json_data.get("condition", [])
        reason = json_data.get("reason")
        line = f"{indent}[Obtain] {{{vars_str}}} such that {{{_format_content(cond)}}}"
        if reason:
            line += f" by {{{_format_content(reason)}}}"
        result_lines.append(line)

    elif node_type == "Define":
        term = json_data.get("term", "")
        defn = json_data.get("definition", "")
        result_lines.append(f"{indent}[Define] {{{term}}} as {{{defn}}}")

    elif node_type == "PlaceHolder":
        text = json_data.get("text", "")
        result_lines.append(f"{indent}[PlaceHolder] {{{text}}}")
        
    elif node_type == "LogicChain":
        init = json_data.get("initial_proposition", [])
        result_lines.append(f"{indent}[LogicChain] {{{_format_content(init)}}}")
        for s in json_data.get("step", []):
            op = s.get("operator", "")
            prop = _format_content(s.get("proposition", []))
            r = s.get("reason")
            l = f"{indent}    {op} {{{prop}}}"
            if r: l += f" by {{{_format_content(r)}}}"
            result_lines.append(l)
            
    elif node_type == "CalculationChain":
        init = json_data.get("initial_expression", [])
        result_lines.append(f"{indent}[CalculationChain] {{{_format_content(init)}}}")
        for s in json_data.get("step", []):
            op = s.get("operator", "")
            expr = _format_content(s.get("expression", []))
            r = s.get("reason")
            l = f"{indent}    {op} {{{expr}}}"
            if r: l += f" by {{{_format_content(r)}}}"
            result_lines.append(l)
            
    elif node_type == "Hint":
        result_lines.append(f"{indent}[Hint] {{{json_data.get('text', '')}}}")
        
    elif node_type == "SufficesToProve":
        content = _format_content(json_data.get("sufficient_proposition", []))
        line = f"{indent}[SufficesToProve] {{{content}}}"
        if json_data.get("reason"):
            line += f" by {{{_format_content(json_data.get('reason'))}}}"
        result_lines.append(line)
        
    elif node_type == "Find":
        content = _format_content(json_data.get("target", []))
        line = f"{indent}[Find] {{{content}}}"
        if json_data.get("condition"):
            line += f" s.t. {{{_format_content(json_data.get('condition'))}}}"
        result_lines.append(line)

    else:
        pass

    if "scope" in json_data:
        result_lines.append(f"{indent}{{")
        result_lines.append(pretty_print_structure(json_data["scope"], indent_level + 1))
        result_lines.append(f"{indent}}}")

    return "\n".join(result_lines)

def pretty_print_json_string(json_input: str) -> str:
    try:
        data = json.loads(json_input)
    except json.JSONDecodeError:
        return "Invalid JSON Format"
    
    if "structure" in data:
        return pretty_print_structure(data["structure"])
    else:
        return pretty_print_structure(data)
    
def extract_json_from_markdown(text: str) -> str:
    pattern_json = r"```json(.*?)```"
    match = re.search(pattern_json, text, re.DOTALL)
    if match:
        return match.group(1).strip()

    pattern_generic = r"```(.*?)```"
    match = re.search(pattern_generic, text, re.DOTALL)
    if match:
        return match.group(1).strip()

    return text.strip()