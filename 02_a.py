from aoc import get_input, get_test_input
import re

DAY = 2
PART = "a"

if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()

    POSSIBLE = {"red": 12, "green": 13, "blue": 14}

    total = 0
    for idx, line in enumerate(data):
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
