"""
Advent of Code 2022 - Day 1 - Part 2
"""

#!/usr/bin/env python

import sys
import os
import re

INPUT = "testdata.txt"
INPUT = "data.txt"

cd = os.path.dirname(__file__)

STRING_ARRAY = ["zero", "one", "two", "three",
                "four", "five", "six", "seven", "eight", "nine"]

if __name__ == "__main__":

    TOTAL = 0
    with open(f"{cd}/{INPUT}", "r", encoding="utf-8") as f:
        for line in f:
            MIN_INDEX = sys.maxsize
            MAX_INDEX = -1
            FIRST_NUM = 0
            LAST_NUM = 0

            # Find first and last numeric char
            try:
                first_numeric_char = re.search(r'\d', line).group()
                index = line.index(first_numeric_char)
                MIN_INDEX = min(MIN_INDEX, index)
                FIRST_NUM = int(first_numeric_char)
            except:
                pass
            try:
                last_numeric_char = re.findall(r'\d', line)[-1]
                index = line.rfind(last_numeric_char)
                MAX_INDEX = max(MAX_INDEX, index)
                LAST_NUM = int(last_numeric_char)
            except:
                pass

            # Find first and last numeric word
            for num in STRING_ARRAY:
                if num in line:
                    num_int = STRING_ARRAY.index(num)

                    min_index = line.index(num)
                    MIN_INDEX = min(MIN_INDEX, min_index)
                    if min_index == MIN_INDEX:
                        FIRST_NUM = num_int

                    max_index = line.rfind(num)
                    MAX_INDEX = max(MAX_INDEX, max_index)
                    if max_index == MAX_INDEX:
                        LAST_NUM = num_int

            # print(f"{FIRST_NUM}{LAST_NUM}")
            TOTAL += int(f"{FIRST_NUM}{LAST_NUM}")

    print(TOTAL)
