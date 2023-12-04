from aoc import get_input, get_test_input
import re

DAY = 3
PART = "b"

def find_kog(char_map, x, y, kog_coords):
    found = False
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (y+dy) >= 0 and (x+dx) >= 0 and (y+dy) < len(char_map)-1 and (x+dx) < len(char_map[0]):
                c = char_map[y+dy][x+dx]
                if c == '*':
                    found = True
                    if (x+dx, y+dy) not in kog_coords:
                        kog_coords.append((x+dx, y+dy))
    
    return found

if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()
    
    char_map = {}
    for y, line in enumerate(data):
        row = {}
        for x, char in enumerate(line.rstrip()):
            row[x] = char
        char_map[y] = row

    kog_map = {}
    kog_count = 0
    for y, line in enumerate(data):
        number = ""
        has_kog = False
        kog_coords = []

        x = 0
        while x < len(line):
            if line[x].isnumeric() and not x == len(line)-1:
                number += line[x]
                if find_kog(char_map, x, y, kog_coords):
                    has_kog = True
            else:
                if line[x].isnumeric() and x == len(line)-1:
                    number += line[x]
                    if find_kog(char_map, x, y, kog_coords):
                        has_kog = True
                
                if has_kog and len(number) > 0:
                    for coord in kog_coords:
                        try:
                            if number not in kog_map[coord]:
                                kog_map[coord].append(number)
                        except:
                            kog_count += 1
                            kog_map[coord] = [number]
                number = ""
                has_kog = False
                kog_coords = []
            x += 1

    ref_count = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '*':
                ref_count[(x, y)] = 1

    # Make sure to find all coordinates
    missing_coordinates = set(ref_count.keys()) ^ set(kog_map.keys())
    for missing_coord in missing_coordinates:
        print("Missing coordinate:", missing_coord)
    
    total = 0
    for k in kog_map:
        if len(kog_map[k]) == 2:
            gear_ratio = 1
            for v in kog_map[k]:
                gear_ratio *= int(v)
            total += gear_ratio

print(total)