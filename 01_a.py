from aoc import get_input, get_test_input
import re

DAY = 1
PART = "a"

if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()

    total = 0
    for line in data:
        first_numeric_char = re.search(r'\d', line).group()
        last_numeric_char = re.findall(r'\d', line)[-1]

        total += int(first_numeric_char + last_numeric_char)

    print(total)
