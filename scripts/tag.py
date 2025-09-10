"""Tag first line of code2vec input files based on mapping file."""
from __future__ import annotations
import os
from config import CODE2VEC_DIR, NEXT_PROBLEM_DIR
 # Removed custom logger usage; using prints.

def main():
    id_to_data: dict[str, str] = {}
    mapping_file = NEXT_PROBLEM_DIR / 'c2v_nextproblem.txt'
    if not mapping_file.is_file():
        print(f"[tag][error] mapping file not found: {mapping_file}")
        return
    for line in mapping_file.read_text(encoding='utf-8').splitlines():
        parts = line.strip().split(None, 2)
        if len(parts) >= 3:
            _id = parts[0]
            data = parts[2]
            id_to_data[_id] = data
    if not CODE2VEC_DIR.exists():
        print(f"[tag][error] directory not found: {CODE2VEC_DIR}")
        return
    for filename in os.listdir(CODE2VEC_DIR):
        if not filename.endswith('.txt'):
            continue
        _id = filename[:-4]
        if _id not in id_to_data:
            continue
        file_path = CODE2VEC_DIR / filename
        lines = file_path.read_text(encoding='utf-8').splitlines(True)
        if not lines:
            continue
        lines[0] = lines[0].replace("program", id_to_data[_id]) + ('\n' if not lines[0].endswith('\n') else '')
    file_path.write_text(''.join(lines), encoding='utf-8')
    print(f"[tag] tagged {_id}")

if __name__ == '__main__':
    main()
