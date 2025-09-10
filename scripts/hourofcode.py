"""Convert trace ids to aggregated project JSON files."""
from __future__ import annotations
import os, json
from pathlib import Path
from blocks_process import process_data
from tree2scr import create_project_data
from config import ASTS_DIR, TRACE_OUTPUT_DIR, NEXT_PROBLEM_DIR, TRAJECTORIES_DIR
# Removed custom logger usage; simple prints are used instead.

def add_blocks(blocks, number):
    if number == 34:
        return
    ast_file = ASTS_DIR / f"{number}.json"
    if not ast_file.is_file():
        return
    try:
        with ast_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
        new_data = process_data(data)
        blocks.update(new_data)
    except Exception as e:
        print(f"[hourofcode][warn] failed to process ast {number}: {e}")
        return

def trace2blocks(student_id, trace_id):
    trace_file = TRAJECTORIES_DIR / f"{trace_id}.txt"
    if not trace_file.is_file():
        return
    numbers = []
    with trace_file.open('r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
                numbers.append(int(line))
    blocks = {}
    for number in numbers:
        add_blocks(blocks, number)
    project_data = create_project_data(blocks)
    TRACE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_json = TRACE_OUTPUT_DIR / f"{student_id}.json"
    with output_json.open('w', encoding='utf-8') as json_file:
        json.dump(project_data, json_file, ensure_ascii=False, indent=4)

def tag_project():
    idmap = NEXT_PROBLEM_DIR / 'c2v_nextproblem.txt'
    if not idmap.is_file():
        raise FileNotFoundError(f"mapping file not found: {idmap}")
    with idmap.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(' ')
            if len(parts) < 3:
                continue
            student_id, tra = parts[0], parts[1]
            trace2blocks(student_id, tra)

if __name__ == '__main__':
    print("[hourofcode] start tag_project")
    tag_project()
    print("[hourofcode] end tag_project")
