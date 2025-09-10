import json
from blocks.id_generate import preprocess_json
from blocks.set_opcode import map_opcodes
from blocks.set_path import set_path
from blocks.set_inputs import set_inputs
from blocks.delete_id import delete_id
from blocks.set_fields import set_fields
from blocks.set_top import set_top

def  process_data(data):
    processed_json, blocks = preprocess_json(data)

    blocks = map_opcodes(blocks)
     
    blocks = set_top(blocks, processed_json)

    blocks = set_path(blocks, processed_json)

    blocks = delete_id(blocks)

    blocks = set_inputs(blocks)

    blocks = set_fields(blocks)

    return blocks
