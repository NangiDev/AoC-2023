"""
Advent of Code 2023 - Day 2 - Part 1
"""

#!/usr/bin/env python

import os
import re

INPUT = "testdata.txt"
INPUT = "data.txt"

POSSIBLE = {"red": 12, "green": 13, "blue": 14}

cd = os.path.dirname(__file__)

if __name__ == "__main__":

    total = 0
    with open(f"{cd}/{INPUT}", "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            a = line[line.index(':')+1:]
            turns = re.split(';|,',a)

            is_game_possible = True
            for t in turns:
                (x, y) = t.split()
                if int(x) > POSSIBLE[y]:
                    is_game_possible = False
                    break
            
            if(is_game_possible):
                total += idx+1

    print(total)
