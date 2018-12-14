import pprint
import re
from tqdm import trange
from helpers import Point

pp = pprint.PrettyPrinter(indent=4)


class Particle:
    acceleration = ...  # type: Point
    position = ...  # type: Point
    velocity = ...  # type: Point

    def __init__(self, position: Point, velocity: Point, acceleration: Point):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.time = 0

    def __repr__(self):
        return "Particle({}, {}, {})".format(*map(repr, [self.position, self.velocity, self.acceleration]))

    def __str__(self):
        return "Particle {}, {}, {}".format(*map(str, [self.position, self.velocity, self.acceleration]))

    def tick(self):
        self.time += 1
        self.velocity += self.acceleration
        self.position += self.velocity


def process_input():
    file = 'x.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    data = [re.findall(r"(-?\d+)", d) for d in data]
    data = [list(map(int, d)) for d in data]
    data = [Particle(Point(a, b, c), Point(d, e, f), Point(g, h, i)) for a, b, c, d, e, f, g, h, i in data]
    return data


def main():
    data = get_input()
    print(list(map(str, data)))


if __name__ == '__main__':

    main()
