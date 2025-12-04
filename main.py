import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from src.structure_gen.generate_structure import main as run_structure_gen
    from src.lean_sketch_gen.generate_lean_sketch import main as run_lean_sketch_gen
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Autoformalization Pipeline Master Controller")
    
    parser.add_argument(
        "--step", 
        type=str, 
        choices=['structure', 'sketch', 'all'], 
        default='all', 
    )
    
    args = parser.parse_args()

    if args.step in ['structure', 'all']:
        print("Running Structure Generation...")
        try:
            run_structure_gen()
        except KeyboardInterrupt:
            print("\nUser interrupted Structure Generation.")
            sys.exit(1)
        except Exception as e:
            print(f"Structure Generation Failed with error: {e}")
            sys.exit(1)

    if args.step in ['sketch', 'all']:
        print("\nRunning Lean Sketch Generation...")
        
        structure_file = os.path.join("display", "structure.json")
        if not os.path.exists(structure_file) and args.step == 'all':
            print(f"Error: {structure_file} not found. Structure generation might have failed.")
            sys.exit(1)
            
        try:
            run_lean_sketch_gen()
        except KeyboardInterrupt:
            print("\nUser interrupted Sketch Generation.")
            sys.exit(1)
        except Exception as e:
            print(f"Lean Sketch Generation Failed with error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()