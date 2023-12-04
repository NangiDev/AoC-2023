from aoc import get_input, get_test_input
import re

DAY = 4
PART = "a"


if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()

    total = 0

    for line in data:
        (win, lot) = line[7:].split('|')
        win = win.strip().replace("  ", ' ').split(' ')
        lot = lot.strip().replace("  ", ' ').split(' ')

        diff = set(win) & set(lot)

        point = 0
        for idx, d in enumerate(diff):
            if idx == 0:
                point = 1
            else:
                point *= 2
        
        total += point

    print(total)

