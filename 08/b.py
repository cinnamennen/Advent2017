import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]

data = [(d + '\n').replace('\n', ' else 0\n').replace('inc', '+=').replace('dec', '-=') for d in data]
m = defaultdict(int)

maximum = 0
for line in data:
    exec(line, {}, m)
    maximum = (max(max(m.values()), maximum))
pp.pprint(maximum)
