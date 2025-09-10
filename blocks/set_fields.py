import json
from blocks.id_generate import generate_id

def set_fields(blocks):
    for block_id, block in list(blocks.items()):
        if block['opcode'] == 'isPathRight':
            new_block_id = generate_id()
            block['opcode'] = 'sensing_keypressed'
            blocks[new_block_id] = {
                "opcode": 'sensing_keyoptions',
                "next": None,
                "parent": block_id,
                "inputs": {},
                "fields": {
                    "KEY_OPTION": [
                        "right arrow",
                        None
                    ]
                },
                "shadow": False,
                "topLevel": False
            }
            block['inputs'] = {
                "KEY_OPTION": [
                    1,
                    new_block_id
                ]
            }
            continue
        if block['opcode'] == 'isPathLeft':
            new_block_id = generate_id()
            block['opcode'] = 'sensing_keypressed'
            blocks[new_block_id] = {
                "opcode": 'sensing_keyoptions',
                "next": None,
                "parent": block_id,
                "inputs": {},
                "fields": {
                    "KEY_OPTION": [
                        "left arrow",
                        None
                    ]
                },
                "shadow": False,
                "topLevel": False
            }
            block['inputs'] = {
                "KEY_OPTION": [
                    1,
                    new_block_id
                ]
            }
            continue
        if block['opcode'] == 'isPathForward':
            new_block_id = generate_id()
            block['opcode'] = 'sensing_keypressed'
            blocks[new_block_id] = {
                "opcode": 'sensing_keyoptions',
                "next": None,
                "parent": block_id,
                "inputs": {},
                "fields": {
                    "KEY_OPTION": [
                        "up arrow",
                        None
                    ]
                },
                "shadow": False,
                "topLevel": False
            }
            block['inputs'] = {
                "KEY_OPTION": [
                    1,
                    new_block_id
                ]
            }
    return blocks