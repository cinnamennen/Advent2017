import collections
import functools


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


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def distance_to(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def zero_distance(self):
        return self.distance_to(0, 0)

    def __repr__(self):
        return "<Point {}>".format(str(self))

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash(repr(self))

    def __iter__(self):
        return iter((self.x, self.y))


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
