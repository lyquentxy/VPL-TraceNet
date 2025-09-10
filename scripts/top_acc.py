"""Compute aggregated accuracy statistics from merged output."""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
from config import NEXT_PROBLEM_DIR, TRAJECTORIES_DIR, GENERATED_DIR
 # Removed custom logger usage; using prints.

def process_data(max_lines: int = 10):
    input_file = NEXT_PROBLEM_DIR / 'c2v_nextproblem.txt'
    if not input_file.is_file():
        raise FileNotFoundError(f"missing file: {input_file}")
    results: list[tuple[int,int,str]] = []
    for line in input_file.read_text(encoding='utf-8').splitlines():
        parts = line.strip().split()
        if len(parts) < 3:
            continue
        trace, complete = parts[1], parts[2]
        traj_file = TRAJECTORIES_DIR / f"{trace}.txt"
        if not traj_file.is_file():
            continue
        lc = sum(1 for _ in traj_file.open('r', encoding='utf-8'))
        if 0 < lc <= max_lines:
            results.append((int(trace), lc, complete))
    results.sort(key=lambda x: x[0])
    out_file = GENERATED_DIR / 'trajectory_line_counts.txt'
    with out_file.open('w', encoding='utf-8') as out:
        for trace, lc, complete in results:
            out.write(f"{trace} {lc} {complete}\n")
    print(f"[top_acc] wrote trajectory counts to {out_file}")
    return out_file

def process_top_acc(merged_filename: str = 'merged_output.txt'):
    merged_path = Path(merged_filename)
    if not merged_path.is_file():
        raise FileNotFoundError(f"missing file: {merged_path}")
    aggregator = defaultdict(lambda: {"count_sum": 0, "acc_sum": 0.0})
    for line in merged_path.read_text(encoding='utf-8').splitlines():
        parts = line.strip().split(' ')
        if len(parts) < 4:
            continue
        completion_type = parts[1]
        count = int(parts[2])
        rel_acc = float(parts[3])
        rel_acc = abs(rel_acc - 0.5) + 0.5
        aggregator[completion_type]["count_sum"] += count
        aggregator[completion_type]["acc_sum"] += count * rel_acc
    for completion_type, info in aggregator.items():
        total_count = info["count_sum"]
        overall_acc = (info["acc_sum"] / total_count) if total_count else 0.0
        print(f"[top_acc] {completion_type} {overall_acc:.2f}")

if __name__ == "__main__":
    process_top_acc()
