from tree2scr import tree2scr

def sample_ast():
    return {
        "type": "program",
        "children": [
            {"type": "program", "children": []},
        ]
    }

def test_tree2scr_structure():
    project = tree2scr(sample_ast())
    assert "targets" in project
    assert len(project["targets"]) == 2
    sprite = project["targets"][1]
    assert "blocks" in sprite
