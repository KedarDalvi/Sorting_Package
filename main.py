#!/usr/bin/env python3
"""
Usage:
    python main.py input.txt

Input file format (4+ lines):
1) algorithm_name  (bubble | selection | merge | quick)
2) order           (asc | desc)
3) size            (integer)
4+) elements       (space separated integers) -- can be on one or multiple lines

Example file:
merge
asc
5
4 1 7 0 -3
"""

import sys
from src.factory import SorterFactory

def parse_input_file(path):
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]
    if len(lines) < 4:
        raise ValueError("Input must have at least 4 non-empty lines.")
    algo = lines[0]
    order = lines[1].lower()
    size = int(lines[2])
    rest = " ".join(lines[3:])
    elems = [int(x) for x in rest.split()]
    if len(elems) != size:
        raise ValueError(f"Declared size {size} but found {len(elems)} elements.")
    return algo, order, size, elems

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py input.txt", file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    algo, order, size, elems = parse_input_file(path)
    ascending = True if order in ("asc", "ascending", "a") else False
    sorter = SorterFactory.get_sorter(algo, ascending=ascending)
    sorted_list = sorter.sort(elems)
    print(" ".join(str(x) for x in sorted_list))

if __name__ == "__main__":
    main()
