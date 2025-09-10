import json
from blocks_process import process_data

def create_project_data(data):
    """Create Scratch-like project data structure with stage + one sprite."""
    project_data = {
        "targets": [
            {
                "isStage": True,
                "name": "Stage",
                "variables": {},
                "lists": {},
                "broadcasts": {},
                "blocks": {},
                "comments": {},
                "currentCostume": 0,
                "costumes": [],
                "sounds": [],
                "volume": 100,
                "layerOrder": 0,
                "tempo": 60,
                "videoTransparency": 50,
                "videoState": "on",
                "textToSpeechLanguage": None
            },
            {
                "isStage": False,
                "name": "Stage",
                "variables": {},
                "lists": {},
                "broadcasts": {},
                "blocks": {},
                "comments": {},
                "currentCostume": 0,
                "costumes": [],
                "sounds": [],
                "volume": 100,
                "layerOrder": 0,
                "tempo": 60,
                "videoTransparency": 50,
                "videoState": "on",
                "textToSpeechLanguage": None
            }

        ],
        "meta": {
            "semver": "3.0.0",
            "vm": "0.2.0",
            "agent": "Mozilla/5.0"
        }
    }

    project_data["targets"][1]["blocks"].update(data)

    return project_data


def tree2scr(data):
    """Convert raw AST dict into simplified Scratch project structure."""
    blocks = process_data(data)
    project_data = create_project_data(blocks)
    return project_data

"""Example usage (pseudo)
from pathlib import Path
import json
from tree2scr import tree2scr

ast = json.loads(Path('data/asts/0.json').read_text(encoding='utf-8'))
project = tree2scr(ast)
Path('data/scripts/0.json').write_text(json.dumps(project, ensure_ascii=False, indent=4), encoding='utf-8')
"""
