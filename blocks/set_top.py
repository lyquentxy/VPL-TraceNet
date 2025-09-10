import json

def _first_non_wrapper(node):
    while node and node.get('type') in ('DO', 'statementList'):
        children = node.get('children') or []
        if not children:
            return None
        node = children[0]
    return node.get('id') if node else None

def set_top(blocks, processed_json):
    root_children = processed_json.get('children') or []
    first_stmt_id = None
    if root_children:
        first_stmt_id = _first_non_wrapper(root_children[0])
    for block in blocks.values():
        if block.get('opcode') == 'event_whenflagclicked':
            block['topLevel'] = True
            if first_stmt_id and first_stmt_id != block.get('id'):
                block['next'] = first_stmt_id
    return blocks

