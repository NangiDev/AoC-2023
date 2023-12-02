"""
Advent of Code 2023 - Day 1 - Part 1
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
        for line in f:
            first_numeric_char = re.search(r'\d', line).group()
            last_numeric_char = re.findall(r'\d', line)[-1]

            total += int(first_numeric_char + last_numeric_char)

    print(total)
