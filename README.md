# Faithful Autoformalization with Structured-Natural-Language

This project implements an autoformalization pipeline based on **Structured Natural Language**. It translates natural language mathematical proofs into **Lean 4** code sketches (formal proofs with gaps).

The system operates in two main stages:

1.  **Structure Generation**: Extracts a structured JSON representation from raw text (using iterative placeholder removal and self-evaluation).
2.  **Lean Sketch Generation**: Translates the JSON structure into Lean 4 code and automatically fixes errors using compiler feedback.

## Environment Setup Guide

This project runs best on **Linux** or **Windows (via WSL2)**. You should also install `python3` (Dependencies include: `openai`, `python-dotenv`, `pydantic`, `httpx`) and `Lean4`.

### Compile Lean Environment

To run the **Lean Sketch Generation** stage, you must first compile the lean environment.

```bash
cd lean_env
lake exe cache get
lake build
cd ..
```

### Configuration (.env)

You need to create a configuration file `.env` in the root directory to store your API keys, paths, and adjust the parameters of the pipeline.

```ini
# LLM API
## Model for JSON to Lean-Sketch Generation
SKETCH_GEN_MODEL=xxx
SKETCH_GEN_API_KEY=sk-xxx
SKETCH_GEN_BASE_URL=xxx
SKETCH_GEN_TEMP=0.2
## Model for Lean Revise
SKETCH_REVISE_MODEL=xxx
SKETCH_REVISE_API_KEY=sk-xxx
SKETCH_REVISE_BASE_URL=xxx
SKETCH_REVISE_TEMP=0.5
## Model for Structure Extraction (Place-Holder fill in)
STRUCTURE_EXTRACT_MODEL=xxx
STRUCTURE_EXTRACT_API_KEY=sk-xxx
STRUCTURE_EXTRACT_BASE_URL=xxx
STRUCTURE_EXTRACT_TEMP=0.2
## Model for Structure Evaluation
STRUCTURE_EVAL_MODEL=deepseek-v3-250324
STRUCTURE_EVAL_API_KEY=sk-xxx
STRUCTURE_EVAL_BASE_URL=xxx
STRUCTURE_EVAL_TEMP=0.1
## Model for Structure Revise
STRUCTURE_REVISE_MODEL=deepseek-v3-250324
STRUCTURE_REVISE_API_KEY=sk-xxx
STRUCTURE_REVISE_BASE_URL=xxx
STRUCTURE_REVISE_TEMP=0.5

# Lean4 Environment
LEAN_PROJECT_ROOT=/path_to_project/MathStructure/lean_env
LEAN_SOURCE_DIR=LeanProject

# Structure Generation
MAX_EXTRACT_ITER=15
MAX_REVISE_ITER=15
STRUCTURE_ACCURACY_THRESHOLD=0.95

# Sketch Generation
MAX_SKETCH_GEN_ITER=15
MAX_SKETCH_REVISE_RETRIES=5

# Whole LLM Log Generation
DEBUG=false
```

## How to Run

All commands should be run from the **project root directory**.

### Prepare Input

Put your informal mathematical proof into the following file:
`display/informal.md`

### Execute

Run the main controller script.

**Run the Full Pipeline:**

```bash
python main.py
```

*(This performs: Structure Extraction -\> JSON Generation -\> Lean Sketch Generation -\> Auto-Correction)*

**Run Only Structure Generation:**

```bash
python main.py --step structure
```

**Run Only Lean Sketch Generation:**
*(Requires `display/structure.json` to exist)*

```bash
python main.py --step sketch
```

## View Results (The `display/` Folder)

This folder acts as your "Dashboard". It contains the real-time inputs and outputs of the system.

  * `informal.md`: The informal proof.
  * `structure.json`: The generated intermediate structure.
  * `structure_pretty.md`: A human-readable version of the structure.
  * `evaluation.json`: The AI judge's score of the structure.
  * `llm_output.lean`: The latest Lean4 sketch output from the LLM.
  * `lean_msg.md`: Latest message returned by the Lean compiler.
  * `lean_sketch.lean`: The Final Lean4 proof sketch.
  * `llm_query_log_.../`: Detailed logs of every prompt sent to the LLM and response received from the LLM.