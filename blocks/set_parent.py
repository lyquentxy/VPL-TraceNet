import json 

def set_parent(blocks, str1, str2):
    blocks[str1]['parent'] = str2

    return blocks