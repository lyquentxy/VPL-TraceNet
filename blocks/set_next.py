import json

def set_next(blocks, str1, str2):
    blocks[str1]['next'] = str2

    return blocks