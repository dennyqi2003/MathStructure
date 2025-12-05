import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.json_utils import create_initial_structure_string, pretty_print_json_string
from utils.no_placeholder import check_no_placeholder
from src.structure_gen.structure_extractor import StructureExtractor
from src.structure_gen.structure_evaluator import StructureEvaluator
from src.structure_gen.structure_reviser import StructureReviser
from src.structure_gen.logger import StructureLogger
from src.structure_gen.evaluation_def import EvaluationResult
from src.structure_gen.node_def import Structure

load_dotenv()

# env
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
MAX_EXTRACT_ITER = int(os.getenv("MAX_EXTRACT_ITER", 15))
MAX_REVISE_ITER = int(os.getenv("MAX_REVISE_ITER", 15))
ACCURACY_THRESHOLD = float(os.getenv("STRUCTURE_ACCURACY_THRESHOLD", 1.0))

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DISPLAY_DIR = os.path.join(PROJECT_ROOT, "display")

def clean_structure_json(json_str: str) -> str:

    try:
        struct_obj = Structure.model_validate_json(json_str)
        return struct_obj.model_dump_json(indent=2, exclude={'thinking'})
    except Exception as e:
        print(f"Warning: Failed to clean JSON (writing raw): {e}")
        return json_str

def main():
    print(f"Starting Structure Generation...")
    print(f"Configs: DEBUG={DEBUG}, Threshold={ACCURACY_THRESHOLD}")
    
    informal_path = os.path.join(DISPLAY_DIR, "informal.md")
    if not os.path.exists(informal_path):
        print(f"Error: {informal_path} not found.")
        return
        
    with open(informal_path, 'r', encoding='utf-8') as f:
        informal_text = f.read()

    logger = StructureLogger(PROJECT_ROOT, debug_mode=DEBUG)
    extractor = StructureExtractor(logger)
    evaluator = StructureEvaluator(logger)
    reviser = StructureReviser(logger)
    
    structure_json_path = os.path.join(DISPLAY_DIR, "structure.json")
    pretty_md_path = os.path.join(DISPLAY_DIR, "structure_pretty.md")
    eval_json_path = os.path.join(DISPLAY_DIR, "evaluation.json")
    
    print("\n- Phase 1: Removing Placeholders...")
    
    current_json = create_initial_structure_string(informal_text)
    
    for i in range(1, MAX_EXTRACT_ITER + 1):
        print(f"  > Iter {i}/{MAX_EXTRACT_ITER}...")
        
        new_json_raw = extractor.extract(current_json, PROJECT_ROOT, i)
        
        if not new_json_raw:
            print("  Extractor returned empty. Retrying...")
            continue
            
        cleaned_json = clean_structure_json(new_json_raw)
        with open(structure_json_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_json)
        
        with open(pretty_md_path, 'w', encoding='utf-8') as f:
            f.write("```text\n" + pretty_print_json_string(cleaned_json) + "\n```")
            
        if check_no_placeholder(cleaned_json):
            print("  No placeholders found. Proceeding to Phase 2.")
            current_json = cleaned_json
            break
        else:
            print("  Placeholders remain. Continuing...")
            current_json = cleaned_json
    else:
        print("  Max extraction iterations reached. Proceeding with potential placeholders.")

    print("\n- Phase 2: Evaluation & Revision...")
    
    TOTAL_POSSIBLE_SCORE = 30
    PASSING_SCORE = TOTAL_POSSIBLE_SCORE * ACCURACY_THRESHOLD
    
    for i in range(1, MAX_REVISE_ITER + 1):
        print(f"  > Cycle {i}/{MAX_REVISE_ITER}...")
        eval_res_str = evaluator.evaluate(informal_text, current_json, PROJECT_ROOT, i)
        if not eval_res_str:
            print("  Evaluation failed. Skipping cycle.")
            continue
            
        with open(eval_json_path, 'w', encoding='utf-8') as f:
            f.write(eval_res_str)
            
        try:
            eval_obj = EvaluationResult.model_validate_json(eval_res_str)
            scores = [
                eval_obj.evaluation.information_equivalency.score,
                eval_obj.evaluation.no_free_variables.score,
                eval_obj.evaluation.concrete_reference.score,
                eval_obj.evaluation.accurate_node_type.score,
                eval_obj.evaluation.accurate_scoping.score,
                eval_obj.evaluation.logical_clarification.score
            ]
            current_total_score = sum(scores)
            print(f"  Scores: {scores} (Total: {current_total_score}/{TOTAL_POSSIBLE_SCORE})")
            
            if current_total_score >= PASSING_SCORE:
                print(f"  Passed! Score {current_total_score} meets threshold {PASSING_SCORE} ({ACCURACY_THRESHOLD*100}%).")
                break
            else:
                print(f"  Target: {PASSING_SCORE}. Continuing revision...")
                
        except Exception as e:
            print(f"   Error parsing scores: {e}")

        revised_json_raw = reviser.revise(informal_text, current_json, eval_res_str, PROJECT_ROOT, i)
        if not revised_json_raw:
            print("  Revision failed.")
            continue
            
        cleaned_revised_json = clean_structure_json(revised_json_raw)
            
        with open(structure_json_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_revised_json)
        with open(pretty_md_path, 'w', encoding='utf-8') as f:
            f.write("```text\n" + pretty_print_json_string(cleaned_revised_json) + "\n```")
            
        current_json = cleaned_revised_json
            
    print("\nStructure Generation Process Finished.")

if __name__ == "__main__":
    main()