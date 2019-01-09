import pprint
import re
from collections import defaultdict
from itertools import combinations

from tqdm import trange
import networkx as nx

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def gen_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge + [(cur, b)]
            yield new
            yield from gen_bridges(new, components)


def get_input():
    data = process_input()
    components = defaultdict(set)
    for l in data:
        a, b = [int(x) for x in l.split('/')]
        components[a].add(b)
        components[b].add(a)
    return components


def main():
    data = get_input()
    # print(data)
    paths = [(len(bridge), sum(a + b for a, b in bridge)) for bridge in gen_bridges(None, data)]
    paths.sort(key=lambda p: (p[0], p[1]), reverse=True)
    # pp.pprint(paths)
    print(paths[0][1])


if __name__ == '__main__':
    main()
