import pprint
import re
from tqdm import trange
from string import ascii_uppercase
from helpers import Point, file_directions

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip('\n') for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    return data


def safe_get(grid, y, x):
    return grid[y][x] if 0 <= y < len(grid) and 0 <= x < len(grid[y]) else ' '


def main():
    data = get_input()
    found = []
    direction = file_directions['down']
    location = Point(0, data[0].index('|'))
    last = location - direction
    i = 0
    while True:
        i += 1
        forward = location + direction
        if safe_get(data, *forward) in ['|', '-'] + list(ascii_uppercase):
            last, location = location, forward
            if safe_get(data, *location) in ascii_uppercase:
                found.append(safe_get(data, *location))
            continue
        elif safe_get(data, *forward) == '+':
            last, location = location, forward
            adjacency = {location + d: safe_get(data, *(location + d)) for d in file_directions.values()}

            # Remove where you've been
            del adjacency[last]

            # Ignore where you cannot go
            adjacency = {k: v for k, v, in adjacency.items() if v not in [' ', '+']}

            # Check yourself
            assert (len(adjacency) == 1)

            n = list(adjacency.keys())[0]
            # print(n-location)
            direction = n - location
            # print(d)
            # exit()
        elif safe_get(data, *forward) == ' ':
            break
        else:
            print("Parsing error")
            break

    print(i)


if __name__ == '__main__':
    main()
