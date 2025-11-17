import os

def concatenate_structure_system_prompt():

    input_file_a = "prompt_components/structure_def_prompt.md"
    input_file_b = "prompt_components/structure_translation_prompt.md"
    output_file_c = "structure_system_prompt.md"

    with open(input_file_a, 'r', encoding='utf-8') as f:
        content_a = f.read()

    with open(input_file_b, 'r', encoding='utf-8') as f:
        content_b = f.read()

    concatenated_content = "# Guide: The Structure of Mathematical Natural Language Texts\n\n"+ content_a + "\n\n" + content_b

    
    with open(output_file_c, 'w', encoding='utf-8') as f:
        f.write(concatenated_content)
    print(f"Successfully concatenated {input_file_a} and {input_file_b} to {output_file_c}")



def concatenate_single_node_formalizer_prompt():

    input_file_a = "prompt_components/structure_def_prompt.md"
    input_file_b = "prompt_components/single_node_formalizer.md"
    output_file_c = "single_node_formalizer_prompt.md"

    with open(input_file_a, 'r', encoding='utf-8') as f:
        content_a = f.read()

    with open(input_file_b, 'r', encoding='utf-8') as f:
        content_b = f.read()

    concatenated_content = "# Lean 4 Sketch Generator\n\n"+ content_a + "\n\n" + content_b

    
    with open(output_file_c, 'w', encoding='utf-8') as f:
        f.write(concatenated_content)
    print(f"Successfully concatenated {input_file_a} and {input_file_b} to {output_file_c}")


if __name__ == "__main__":
    concatenate_structure_system_prompt()
    concatenate_single_node_formalizer_prompt()