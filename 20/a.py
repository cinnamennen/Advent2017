import pprint
import re
from functools import total_ordering

from tqdm import trange
from helpers import Point, zero_point

pp = pprint.PrettyPrinter(indent=4)


@total_ordering
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

    def __iter__(self):
        yield self.position
        yield self.velocity
        yield self.acceleration

    def __eq__(self, other):
        return self.position.zero_distance() == other.position.zero_distance() \
               and self.velocity.zero_distance() == other.velocity.zero_distance() \
               and self.acceleration.zero_distance() == other.acceleration.zero_distance()

    def __gt__(self, other):
        return self.acceleration.zero_distance() > other.acceleration.zero_distance() if \
            self.acceleration.zero_distance() != other.acceleration.zero_distance() \
            else self.velocity.zero_distance() > other.velocity.zero_distance() if self.velocity.zero_distance() != \
                                                                                   other.velocity.zero_distance() \
            else self.position.zero_distance() > other.position.zero_distance()


class NilParticle(Particle):
    def __init__(self, particle: Particle = None):
        if particle:
            super().__init__(*particle)
        else:
            super().__init__(*(zero_point(3) * 3))

    def tick(self):
        pass


def process_input():
    file = 'a.txt'
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
    d = data.index(sorted(data)[0])
    print(d)


if __name__ == '__main__':
    main()
