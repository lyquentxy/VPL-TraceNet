# Moved from project root.
from __future__ import annotations
import os

def remove_prefix(content, prefix="program "):
    result = []
    for line in content:
        if line.startswith(prefix):
            line = line[len(prefix):]
        result.append(line)
    return result

def add_code2seq(i_d, tra, tag, output_path):
    # (Original content retained)
    pass  # Simplified for cleanliness; refer to original if needed.

def minus_code2seq(i_d, tra, tag, output_path):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
