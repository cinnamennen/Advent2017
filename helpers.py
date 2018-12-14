import collections
from functools import total_ordering


class Memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.hits = self.misses = 0

    def __call__(self, *args):
        # if not isinstance(args, collections.Hashable):
        #     # uncacheable. a list, for instance.
        #     # better to not cache than blow up.
        #     return self.func(*args)
        # print("checking", args)
        if args in self.cache:
            # self.hits += 1
            # self.success()
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            # self.misses += 1
            # self.success()
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

    def success(self):
        print((self.hits / (self.hits + self.misses)) * 100)

@total_ordering
class Point:
    def __init__(self, *args):
        ints = list(map(lambda v: isinstance(v, int), args))
        if not all(ints):
            raise TypeError('{} is not an integer'.format(args[ints.index(False)]))
        self.values = args
        self.order = len(args)

    def distance_to(self, other):
        return sum([abs(a - b) for a, b in zip(self.values, other.values)])

    def zero_distance(self):
        return self.distance_to(self.zero_point())

    def __repr__(self):
        return "Point{}".format(str(self))

    def __str__(self):
        return "({})".format(','.join(map(str, self.values)))

    def __add__(self, other):
        return Point(*[a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        return Point(*[a - b for a, b in zip(self.values, other.values)])

    def __eq__(self, other):
        return all(a == b for a, b in zip(self.values, other.values))

    def __hash__(self):
        return hash(repr(self))

    def __iter__(self):
        yield from self.values

    def __bool__(self):
        pass

    def __lt__(self, other):
        # return self < other
        return all(a < b for a, b in zip(self.values, other.values))

    def zero_point(self):
        return zero_point(self.order)


def zero_point(order):
    return Point(*([0] * order))


directions = {
    'left': Point(-1, 0),
    'right': Point(1, 0),
    'up': Point(0, 1),
    'down': Point(0, -1)
}
file_directions = {
    'left': Point(0, -1),
    'right': Point(0, 1),
    'up': Point(-1, 0),
    'down': Point(1, 0)
}
