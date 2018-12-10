import collections
import functools
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]


def score(s):
    level = 0
    total = 0
    for c in s:
        if c == '{':
            level += 1
        if c == '}':
            total += level
            level -= 1
    return total


new_data = []
for line in data:
    token = line
    # Cancel out according to !
    token = re.sub(r"(!.)", '', token)
    token = re.findall(r"(<.*?>)", token)

    token = [len(t) -2 for t in token]
    # token = re.sub(r"(,,+)", '', token)
    # token = re.sub(r"(,)", '', token)
    new_data.append(sum(token))

data = new_data

pp.pprint(data)
