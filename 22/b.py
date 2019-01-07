import enum
import pprint
import re
from collections import defaultdict

from cinnamon_tools.point import Point
from tqdm import trange

pp = pprint.PrettyPrinter(indent=4)


class Node(enum.Enum):
    clean = '.'
    weakened = 'W'
    infected = '#'
    flagged = 'F'

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.value

    def cycle(self):
        c = list(Node).index(self) + len(list(Node))
        rv = list(Node)[(c + 1) % len(list(Node))]
        # print(f"{str(self)} -> {str(rv)}")
        return rv


class Turn(enum.Enum):
    left = 'left'
    right = 'right'


class Direction(enum.Enum):
    north = Point(0, -1)
    east = Point(1, 0)
    south = Point(0, 1)
    west = Point(-1, 0)

    def turn(self, turn: Turn):
        c = list(Direction).index(self) + 4
        if turn == Turn.left:
            return list(Direction)[(c - 1) % len(list(Direction))]
        elif turn == Turn.right:
            return list(Direction)[(c + 1) % len(list(Direction))]


class Virus:
    def __init__(self, grid, position=Point(0, 0), direction=Direction.north):
        self.direction = direction
        self.position = position
        self.grid = grid

    def burst(self):
        if self.grid[self.position] == Node.clean:
            self.direction = self.direction.turn(Turn.left)
        elif self.grid[self.position] == Node.weakened:
            pass
        elif self.grid[self.position] == Node.infected:
            self.direction = self.direction.turn(Turn.right)
        elif self.grid[self.position] == Node.flagged:
            self.direction = self.direction.turn(Turn.left).turn(Turn.left)
        else:
            raise AttributeError

        self.grid[self.position] = self.grid[self.position].cycle()

        if self.grid[self.position] == Node.infected:
            rv = True
        else:
            rv = False
        self.position += self.direction.value

        return rv

    def __str__(self):
        # print(self.position)
        min_x = min(self.grid.keys(), key=lambda p: p.x).x
        min_y = min(self.grid, key=lambda p: p.y).y
        max_x = max(self.grid, key=lambda p: p.x).x
        max_y = max(self.grid, key=lambda p: p.y).y
        points = ([(['[' + str(self.grid[Point(x, y)]) + ']' if Point(x, y) == self.position else ' ' + str(
            self.grid[Point(x, y)]) + ' ' for
                     x in range(min_x, max_x + 1)]) for y in range(min_y, max_y + 1)])
        points = '\n'.join([''.join([x for x in y]) for y in points])
        # print(points)

        # print(min_x, min_y)
        return points


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    data = list(map(list, data))
    b = len(data)
    a = len(data[0])
    b = (b - 1) // 2
    a = (a - 1) // 2
    new_data = defaultdict(lambda: Node.clean)
    for y in range(len(data)):
        for x in range(len(data[y])):
            # print(data[y][x])
            new_data[Point(x - a, y - b)] = Node(data[y][x])

    return new_data


def main():
    grid = get_input()
    v = Virus(grid=grid)
    # print(v)
    # exit()
    i = 0
    for _ in trange(10000000):
        if v.burst():
            i += 1
        # print()
        # print(v)
    # print(v.position, grid[v.position])
    print(i)


if __name__ == '__main__':
    main()
