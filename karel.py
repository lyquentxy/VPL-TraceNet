import json
import re


program_tokens = [
    "DEF",
    "run",
    "m(",
    "IFELSE",
    "c(",
    "not",
    "c(",
    "leftIsClear",
    "c)",
    "c)",
    "i(",
    "IFELSE",
    "c(",
    "noMarkersPresent",
    "c)",
    "i(",
    "putMarker",
    "i)",
    "ELSE",
    "e(",
    "move",
    "e)",
    "i)",
    "ELSE",
    "e(",
    "putMarker",
    "turnLeft",
    "e)",
    "move",
    "IFELSE",
    "c(",
    "rightIsClear",
    "c)",
    "i(",
    "pickMarker",
    "i)",
    "ELSE",
    "e(",
    "putMarker",
    "e)",
    "m)"
]


processed_tokens = []
for token in program_tokens:
    if re.match(r'^[a-zA-Z]\($', token) or re.match(r'^[a-zA-Z]\)$', token):
        continue
    processed_tokens.append(token)

def parse_tokens(tokens):
    stack = []
    root = {"type": "program", "id": "11", "children": []}
    current = root
    stack.append(current)
    id_counter = 12

    for token in tokens:
        if token.endswith("("):
            node_type = token[:-1].lower()
            node = {"id": str(id_counter), "type": node_type, "children": []}
            id_counter += 1
            current["children"].append(node)
            stack.append(node)
            current = node
        elif token == ")":
            stack.pop()
            if stack:
                current = stack[-1]
        else:
            if token.upper() in ["IFELSE", "DO", "ELSE"]:
                node = {"id": str(id_counter), "type": token.lower(), "children": []}
                id_counter += 1
                current["children"].append(node)
                stack.append(node)
                current = node
            else:
                node = {"id": str(id_counter), "type": token}
                id_counter += 1
                current["children"].append(node)

    return root

def demo():
    parsed_json = parse_tokens(processed_tokens)
    print(json.dumps(parsed_json, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    demo()