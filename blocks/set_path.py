from . import set_next

def set_path(blocks, json_data, parent_id=None, prev_root_id=None):
    json_children = json_data.get('children', [])
   
    json_type = json_data['type']

    json_id = json_data['id']
    if json_type == 'maze_ifElse':
        condition_node = json_children[0]

        true_branch = json_children[1]
        true_branch_id = true_branch['children'][0]['id']

        false_branch = json_children[2]
        false_branch_id = false_branch['children'][0]['id']

        blocks[json_id]['inputs'] = {
            'CONDITION': [2, condition_node['id']],
            'SUBSTACK': [2, true_branch_id],
            'SUBSTACK2': [2, false_branch_id]
        }

        set_path(blocks, condition_node, parent_id=json_id)
        set_path(blocks, true_branch, parent_id=json_id)
        set_path(blocks, false_branch, parent_id=json_id)

        blocks[condition_node['id']]['parent'] = json_id
        blocks[true_branch['id']]['parent'] = json_id
        blocks[false_branch['id']]['parent'] = json_id

    elif json_type in ['DO', 'ELSE', 'statementList']:
        for i, child in enumerate(json_children):
            set_path(blocks, child, parent_id=json_id, prev_root_id=json_id)
            blocks[child['id']]['parent'] = json_id

            if i < len(json_children) - 1:
                blocks[child['id']]['next'] = json_children[i + 1]['id']
            else:
                blocks[child['id']]['next'] = None
        if json_children:
            blocks[json_id]['next'] = json_children[0]['id']

    elif json_type == 'program':
        if json_children:
            set_path(blocks, json_children[0], parent_id=json_id)

    else:
        if json_children:
            for i, child in enumerate(json_children):
                set_path(blocks, child, parent_id=json_id)
                blocks[child['id']]['parent'] = json_id

                if i < len(json_children) - 1:
                    blocks[child['id']]['next'] = json_children[i + 1]['id']
                else:
                    blocks[child['id']]['next'] = None
            blocks[json_id]['next'] = json_children[0]['id']
        else:
            pass

    if json_type in ['maze_forever', 'maze_ifElse'] or not json_children:
        blocks[json_id]['next'] = None

    return blocks