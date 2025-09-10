import json

def set_inputs(blocks):
    for block_id, block in list(blocks.items()):
        if block['opcode'] == 'motion_movesteps':
            block['inputs'] = {
                "STEPS": [
                    1,
                    [
                        4,
                        "1"
                    ]
                ]
            }
        elif block['opcode'] == 'motion_turnright':
            block['inputs'] = {
                "DEGREES": [
                    1,
                    [
                        4,
                        "90"
                    ]
                ]
            }
        elif block['opcode'] == 'motion_turnleft':
            block['inputs'] = {
                "DEGREES": [
                    1,
                    [
                        4,
                        "90"
                    ]
                ]
            }
        elif block['opcode'] == 'control_forever':
            child_ids = [child_id for child_id, child_block in blocks.items() if child_block.get('parent') == block_id]
            if child_ids:
                first_child_id = child_ids[0]
                block['inputs'] = {"SUBSTACK": [2, first_child_id]}
            else:
                block['inputs'] = {"SUBSTACK": [2, None]}
    return blocks
