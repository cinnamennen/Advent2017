import collections
import functools


class memoized(object):
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
