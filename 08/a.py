import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]

data = [(d + '\n').replace('\n', ' else 0\n').replace('inc', '+=').replace('dec', '-=') for d in data]
m = defaultdict(int)
for line in data:
    exec(line, {}, m)
pp.pprint(max(m.values()))
