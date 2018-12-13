import pprint
from typing import List

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'x.txt'
    data = [_.strip().split(',') for _ in open(file).readlines()]
    data = [list(map(lambda x: directions[x], d)) for d in data]
    # data = [[HexPoint(0,0,0)]+d for d in data]
    return data


class HexPoint:
    def __init__(self, x, y, z):
        self.y = y
        self.x = x
        self.z = z

    def distance_to_coords(self, x, y, z):
        return (abs(self.x - x) + abs(self.y - y) + abs(self.z - z)) / 2

    def distance_to_point(self, p):
        return self.distance_to_coords(*p)

    def zero_distance(self):
        return self.distance_to_point(HexPoint(0, 0, 0))

    def __repr__(self):
        return "<Point ({}, {}, {})>".format(self.x, self.y, self.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        return HexPoint(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __hash__(self):
        return hash(self.__repr__())

    def __iter__(self):
        return iter((self.x, self.y, self.z))


N = HexPoint(0, 1, -1)
NE = HexPoint(1, 0, -1)
SE = HexPoint(1, -1, 0)
S = HexPoint(0, -1, 1)
SW = HexPoint(-1, 0, 1)
NW = HexPoint(-1, 1, 0)

directions = {'n': N, 'ne': NE, 'se': SE, 's': S, 'sw': SW, 'nw': NW}


def get_max_distance(l: List[HexPoint]):
    start = HexPoint(0,0,0)
    n = [sum(l[:t]) for t in range(1,len(l)+1)]
    n = [d.zero_distance() for d in n]
    return max(n)



def main():
    data = process_input()
    data = [get_max_distance(d) for d in data]

    pp.pprint(data)


if __name__ == '__main__':
    main()
