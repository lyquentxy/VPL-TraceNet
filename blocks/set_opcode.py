import json

opcode_mapping = {
    'program': 'event_whenflagclicked',
    "maze_moveForward": "motion_movesteps",
    "maze_turn": "motion_turn",
    "maze_forever": "control_forever",
    "turnleft": "motion_turnleft",
    "turnright": "motion_turnright",
    "maze_ifElse": "control_if_else",
    "DEF": "event_whenflagclicked",
    "MOVE": "motion_movesteps",
    "IFELSE": "control_if_else",
    "leftIsClear": "motion_turnleft",
    "rightIsClear": "motion_turnright",
    "noMarkersPresent": "sensing_touchingobject",
}

def map_opcodes(blocks):
    for block_id, block in blocks.items():
        if 'opcode' in block and block['opcode'] in opcode_mapping:
            block['opcode'] = opcode_mapping[block['opcode']]
    return blocks
