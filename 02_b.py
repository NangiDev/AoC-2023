from aoc import get_input, get_test_input
import re

DAY = 2
PART = "b"

if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()

    total = 0
    for idx, line in enumerate(data):
        POSSIBLE = {"red": 0, "green": 0, "blue": 0}
        a = line[line.index(':')+1:]
        turns = re.split(';|,',a)

        for t in turns:
            (x, y) = t.split()
            POSSIBLE[y] = max(int(x), POSSIBLE[y])
        
        total += POSSIBLE["red"] * POSSIBLE["blue"] * POSSIBLE["green"]

    print(total)
