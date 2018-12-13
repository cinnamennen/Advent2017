import pprint
import re

import networkx as nx

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data

def get_input():
    data = process_input()
    data = [re.findall(r"(\d*)", d) for d in data]
    data = [list(filter(lambda x: x != '', d)) for d in data]

    return data

def main():
    data = get_input()

    G = nx.Graph()

    for r, *n in data:
        for e in n:
            G.add_edge(r, e)
    print((nx.number_connected_components(G)))



if __name__ == '__main__':
    main()
