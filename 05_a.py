from aoc import get_input, get_test_input
import sys

DAY = 5
PART = "a"


MAPS = {}


def convert(t, i):
    try:
        for item in MAPS[t]:
            (s, rng) = MAPS[t][item]

            if i >= item and i < item + rng:
                return s + i - item

        return i
    except:
        return i


if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()

    seeds = []

    current_map = ""
    idx = -1
    while idx < len(data)-1:
        idx += 1
        line = data[idx]

        if len(line) == 0:
            continue

        if idx == 0:
            for seed in line[7:].split(' '):
                seeds.append(int(seed))
            continue

        if "map:" in line:
            current_map = line[0:-5]
            MAPS[current_map] = {}

        if line[0].isdigit():
            r = line.split(' ')

            MAPS[current_map][int(r[1])] = (int(r[0]), int(r[2]))

    map_names = ["seed-to-soil",
                 "soil-to-fertilizer",
                 "fertilizer-to-water",
                 "water-to-light",
                 "light-to-temperature",
                 "temperature-to-humidity",
                 "humidity-to-location"]

    lowert_loc = sys.maxsize
    for seed in seeds:
        source = seed
        for name in map_names:
            source = convert(name, source)
        lowert_loc = min(lowert_loc, source)

    print()
    print(lowert_loc)
