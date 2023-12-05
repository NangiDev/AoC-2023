from aoc import get_input, get_test_input
import cProfile
import time

DAY = 5
PART = "b"


MAPS = {}


def convert_old(t, i):
    try:
        if i in set(MAPS[t]) and not isinstance(MAPS[t][i], tuple):
            return MAPS[t][i]

        for item in MAPS[t]:
            (s, rng) = MAPS[t][item]

            if i >= item and i < item + rng:
                new_val = s + i - item
                MAPS[t][i] = new_val
                return new_val

        MAPS[t][i] = i
        return i
    except:
        MAPS[t][i] = i
        return i


def convert(t, i):
    try:
        item_data = MAPS[t].get(i)

        if item_data is not None and not isinstance(item_data, tuple):
            return item_data

        for item, (s, rng) in MAPS[t].items():
            if item <= i < item + rng:
                new_val = s + i - item
                MAPS[t][i] = new_val
                return new_val

        MAPS[t][i] = i
        return i

    except KeyError:
        MAPS[t][i] = i
        return i
    except:
        return i

    return i

# if __name__ == "__main__":


def main():
    # data = get_input(DAY).splitlines()
    data = get_test_input(PART, DAY).splitlines()

    seeds = []

    current_map = ""
    idx = -1
    while idx < len(data)-1:
        idx += 1
        line = data[idx]

        if not line:
            continue

        if idx == 0:
            z = line[7:].split(' ')

            for i in range(0, len(z), 2):
                seeds.append((int(z[i]), int(z[i+1])))
            seeds = [(int(z[i]), int(z[i+1])) for i in range(0, len(z), 2)]
            continue

        if "map:" in line:
            current_map = line[:-5]
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

    lowest_loc = float('inf')
    checked_sources = set()
    for seed in seeds:
        base_source = seed[0]
        for i in range(seed[1]):
            source = base_source + i
            if source in checked_sources:
                continue
            checked_sources.add(source)
            for name in map_names:
                source = convert(name, source)
            lowest_loc = min(lowest_loc, source)

    print(lowest_loc)


cProfile.run('main()')
exit()

# Set the maximum runtime in seconds
max_runtime = 1  # Adjust this to your desired maximum runtime

# Start the profiler
profiler = cProfile.Profile()
profiler.enable()

# Run your function
start_time = time.time()
while (time.time() - start_time) < max_runtime:
    main()

# Stop the profiler
profiler.disable()

# Print the profiling results
profiler.print_stats()
