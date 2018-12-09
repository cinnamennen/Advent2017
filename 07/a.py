import pprint
import re
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

pp = pprint.PrettyPrinter(indent=4)
file = 'x.txt'
data = [_.strip() for _ in open(file).readlines()]
data = [re.search(r"(.*) \((\d*)\)(?: -> (.*))?", d).groups() for d in data]
data = [(a, b, c.split(', ') if c else []) for (a, b, c) in data]

pp.pprint(data)

graph = nx.DiGraph()
for n, w, c in data:
    graph.add_node(n, weight=w)
    for e in c:
        graph.add_edge(n, e)

nx.draw(graph,graphviz_layout(graph, prog='dot'), with_labels=True)
plt.show()
