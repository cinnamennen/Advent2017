import itertools
import pprint
import re
from hashing import kh
import networkx as nx

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    data = data[0]

    return data


def safe_get(hashes, x, y):
    return hashes[y][x] if 0 <= y < len(hashes) and 0 <= x < len(hashes[y]) else '0'


def main():
    data = get_input()
    hashes = [kh("{}-{}".format(data, n)) for n in range(128)]
    # print(hashes)
    hashes = [bin(int(h, 16))[2:].zfill(128) for h in hashes]
    hashes = [list(h) for h in hashes]

    G = nx.Graph()

    for y in range(128):
        for x in range(128):
            if hashes[y][x] == '1':
                G.add_node('{},{}'.format(x, y))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for y in range(128):
        for x in range(128):
            if safe_get(hashes, x, y) == '0':
                continue
            for check in directions:
                if safe_get(hashes, x + check[0], y + check[1]) == '1':
                    G.add_edge('{},{}'.format(x, y), '{},{}'.format(x + check[0], y + check[1]))
    print((nx.number_connected_components(G)))


if __name__ == '__main__':
    main()
