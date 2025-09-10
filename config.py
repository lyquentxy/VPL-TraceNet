"""Central configuration for dataset paths.

Override defaults by setting environment variable HOC_DATASET_PATH.
All generated outputs should go under BASE_DATASET_PATH / generated.
"""
from __future__ import annotations
from pathlib import Path
import os

BASE_DATASET_PATH = Path(os.getenv("HOC_DATASET_PATH", "data"))
ASTS_DIR = BASE_DATASET_PATH / "asts"
SCRIPTS_DIR = BASE_DATASET_PATH / "scripts"
TRAJECTORIES_DIR = BASE_DATASET_PATH / "trajectories"
NEXT_PROBLEM_DIR = BASE_DATASET_PATH / "nextProblem"
TRACE_OUTPUT_DIR = BASE_DATASET_PATH / "trace"
CODE2SEQ_DIR = BASE_DATASET_PATH / "c2s"
CODE2VEC_DIR = BASE_DATASET_PATH / "code2vec"
GENERATED_DIR = BASE_DATASET_PATH / "generated"

# Ensure directories (non-destructive)
for _p in [GENERATED_DIR]:
    _p.mkdir(parents=True, exist_ok=True)
