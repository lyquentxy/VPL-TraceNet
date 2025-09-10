import json

to_delete = []

def delete_id(blocks):
    def delete_id_recursive(blocks):
        to_delete = []
        for block_id, block in blocks.items():
            if block['opcode'] in ['turnLeft', 'turnRight']:
                parent_id = block.get('parent')
                if parent_id and parent_id in blocks:
                    parent_block = blocks[parent_id]
                    if block['opcode'] == 'turnLeft':
                        parent_block['opcode'] = 'motion_turnleft'
                    elif block['opcode'] == 'turnRight':
                        parent_block['opcode'] = 'motion_turnright'
                to_delete.append(block_id)
        for block_id in to_delete:
            del blocks[block_id]
    return blocks

    def delete_do_statement_else(blocks):
        to_delete = []
        for block_id, block in blocks.items():
            if block['opcode'] == 'DO' or block['opcode'] == 'statementList' or block['opcode'] == 'ELSE' or block['opcode'] == 'DEF' or block['opcode'] == 'RUN':
                for next_block_id, next_block in blocks.items():
                    if next_block.get('parent') == block_id:
                        next_block['parent'] = block.get('parent')
                to_delete.append(block_id)
        for block_id in to_delete:
            del blocks[block_id]
    return blocks

    blocks = delete_id_recursive(blocks)
    blocks = delete_do_statement_else(blocks)
    return blocks