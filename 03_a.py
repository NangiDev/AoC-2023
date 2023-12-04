from aoc import get_input, get_test_input
import re

DAY = 3
PART = "a"

def find_adj(char_map, x, y):
    has_adj = False
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            try:
                c = char_map[x+dx][y+dy]
                if not (c.isnumeric() or c == "."):
                    has_adj = True
            except:
                pass
    return has_adj

if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()

    char_map = {}
    total = 0
    num = ""
    has_adj = False

    for y, line in enumerate(data):
        row = {}
        for x, c in enumerate(line.rstrip()):
            row[x] = c
        char_map[y] = row

    for x in char_map:
        for y in char_map[x]:
            c = char_map[x][y]
            if not c.isnumeric():
                if num != "" and has_adj:
                    total += int(num)
                num = ""
                has_adj = False
                continue

            num += c
            if find_adj(char_map, x, y):
                has_adj = True

    print(total)
