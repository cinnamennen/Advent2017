from itertools import permutations

file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]

data = [list(map(int, _.split())) for _ in data]


def get_divis(r):
    for n, d in permutations(r, 2):
        if n % d == 0:
            return n // d


data = [get_divis(row) for row in data]

data = sum(data)
print(data)
