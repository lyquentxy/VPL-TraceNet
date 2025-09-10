"""Generate c2v_nextproblem.txt from idMap / attempt / perfect sets."""
from __future__ import annotations
from pathlib import Path
from config import TRAJECTORIES_DIR, NEXT_PROBLEM_DIR
 # Removed custom logger usage; using prints.

def process_files():
    idmap_path = TRAJECTORIES_DIR / 'idMap.txt'
    attempts_path = NEXT_PROBLEM_DIR / 'attemptSet.txt'
    perfect_path = NEXT_PROBLEM_DIR / 'perfectSet.txt'
    output_path = NEXT_PROBLEM_DIR / 'c2v_nextproblem.txt'

    attempts = set(p.strip() for p in attempts_path.read_text(encoding='utf-8').splitlines() if p.strip())
    perfect = set(p.strip() for p in perfect_path.read_text(encoding='utf-8').splitlines() if p.strip())

    lines = idmap_path.read_text(encoding='utf-8').splitlines()[1:]
    with output_path.open('w', encoding='utf-8') as output_file:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) < 2:
                continue
            student_id, ast = parts[0], parts[1]
            json_filepath = TRAJECTORIES_DIR / f"{ast}.txt"
            if not json_filepath.is_file():
                continue
            if student_id in perfect:
                marker = 'pft'
            elif ast in attempts:
                marker = 'att'
            else:
                marker = 'def'
            text = json_filepath.read_text(encoding='utf-8').splitlines()
            last_line = text[-1].strip() if text else ''
            flag = 'T' if last_line == '0' else 'F'
            output_file.write(f"{student_id} {ast} {marker} {flag}\n")

    return output_path

if __name__ == '__main__':
    p = process_files()
    print(f"[cleaning] written: {p}")
