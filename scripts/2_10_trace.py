"""Group trajectory files by number of lines within a range."""
from __future__ import annotations
import os
from pathlib import Path
from config import TRAJECTORIES_DIR
 # Removed custom logger usage; using prints.

def group(min_len: int = 2, max_len: int = 10, output_filename: str = "grouped_files.txt"):
    directory: Path = TRAJECTORIES_DIR
    if not directory.exists():
        raise FileNotFoundError(f"trajectory directory not found: {directory}")
    counts_map: dict[int, list[str]] = {n: [] for n in range(min_len, max_len + 1)}
    for fname in os.listdir(directory):
        if not fname.endswith(".txt") or not fname[:-4].isdigit():
            continue
        file_path = directory / fname
        with file_path.open("r", encoding="utf-8") as f:
            c = sum(1 for _ in f)
        if min_len <= c <= max_len:
            counts_map[c].append(fname[:-4])
    out_path = directory / output_filename
    with out_path.open("w", encoding="utf-8") as f:
        f.write("\n")
        for n in range(min_len, max_len + 1):
            f.write(",".join(counts_map[n]) + "\n")
    return out_path

if __name__ == '__main__':
    p = group()
    print(f"[2_10_trace] written: {p}")
