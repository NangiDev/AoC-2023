"""
Advent of Code 2023 - Day 2 - Part 1
"""

#!/usr/bin/env python

import os
import re

INPUT = "testdata.txt"
INPUT = "data.txt"


cd = os.path.dirname(__file__)

if __name__ == "__main__":

    total = 0
    with open(f"{cd}/{INPUT}", "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            POSSIBLE = {"red": 0, "green": 0, "blue": 0}
            a = line[line.index(':')+1:]
            turns = re.split(';|,',a)

            for t in turns:
                (x, y) = t.split()
                POSSIBLE[y] = max(int(x), POSSIBLE[y])
            
            total += POSSIBLE["red"] * POSSIBLE["blue"] * POSSIBLE["green"]


    print(total)
