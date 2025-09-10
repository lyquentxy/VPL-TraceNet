import json
import logging
from pathlib import Path
from tree2scr import tree2scr
from config import ASTS_DIR, SCRIPTS_DIR

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def iter_ast_files():
    if not ASTS_DIR.exists():
        logging.error(f"AST directory not found: {ASTS_DIR}")
        return
    for p in ASTS_DIR.glob('*.json'):
        if p.stem.isdigit():
            yield p

def tree2block_all(limit: int | None = None):
    SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for ast_path in iter_ast_files():
        if limit is not None and count >= limit:
            break
        try:
            with ast_path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            project_data = tree2scr(data)
            out_path = SCRIPTS_DIR / f"{ast_path.stem}.json"
            with out_path.open('w', encoding='utf-8') as f_out:
                json.dump(project_data, f_out, ensure_ascii=False, indent=4)
            if count % 500 == 0:
                logging.info(f"processed {count} files (latest: {ast_path.name})")
            count += 1
        except Exception as e:
            logging.warning(f"skip {ast_path.name}: {e}")
    logging.info(f"done, processed {count} AST files")

if __name__ == "__main__":
    tree2block_all()
