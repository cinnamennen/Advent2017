import itertools
import pprint
from math import floor, ceil

pp = pprint.PrettyPrinter(indent=4)


class Point:

    def __init__(self, x, y):
        self.y = y
        self.x = x

    def distance_to(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def zero_distance(self):
        return self.distance_to(0, 0)

    def __repr__(self):
        return f"<Point ({self.x}, {self.y})>"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")


num = 289326
dir_index = 0

LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
UP = Point(0, 1)
DOWN = Point(0, -1)

directions = [RIGHT, UP, LEFT, DOWN]
adjacency = directions + [RIGHT + UP, RIGHT + DOWN, LEFT + UP, LEFT + DOWN]


def move():
    global dir_index
    rv = directions[dir_index]
    dir_index += 1
    dir_index %= len(directions)
    return rv


memory = {}


def process(p: Point):
    global memory

    if p in memory:
        return memory[p]
    else:
        if p == Point(0, 0):
            memory[p] = 1
        else:
            check = [p + d for d in adjacency]
            check = [memory[c] for c in check if c in memory]
            memory[p] = sum(check)
        return memory[p]


n = 1
starting = Point(0, 0)
location = Point(0, 0)
for x in itertools.count(0, .5):
    # print(ceil(x))
    if ceil(x) == 0:
        process(location)
        continue
    direction = move()

    for _ in range(ceil(x)):
        location += direction
        n += 1
        if process(location) > num:
            print(memory[location])
            exit()
