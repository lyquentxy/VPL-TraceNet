import json
import random
import string

ALPHABET = string.ascii_letters + string.digits

def generate_id():
    return ''.join(random.choices(ALPHABET, k=20))

def assign_ids(node, blocks):
    if 'type' in node:
        node_id = generate_id()
        node['id'] = node_id
        blocks[node_id] = {
            "opcode": node['type'],
            "next": None,
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": False
        }
    if 'children' in node:
        for child in node['children']:
            assign_ids(child, blocks)

def preprocess_json(json_data):
    blocks = {}
    assign_ids(json_data, blocks)
    return json_data, blocks