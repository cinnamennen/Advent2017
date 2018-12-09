import pprint
import re
from collections import Counter

import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

pp = pprint.PrettyPrinter(indent=4)
file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]
data = [re.search(r"(.*) \((\d*)\)(?: -> (.*))?", d).groups() for d in data]
data = [(a, b, c.split(', ') if c else []) for (a, b, c) in data]

graph = nx.DiGraph()
for n, w, c in data:
    graph.add_node(n, weight=int(w))
    for e in c:
        graph.add_edge(n, e)

# Keep track of each node's total weight (itself + its children)
weights = {}
ordered = list(nx.topological_sort(graph))
# Going backwards (starting from the leaves)
for node in reversed(ordered):
    # Start with this nodes own weight
    total = graph.nodes[node]['weight']

    counts = Counter(weights[child] for child in graph[node])
    unbalanced = None

    for child in graph[node]:
        # If this child's weight is different than others, we've found it
        if len(counts) > 1 and counts[weights[child]] == 1:
            unbalanced = child
            break

        # Otherwise add to the total weight
        val = weights[child]
        total += weights[child]

    if unbalanced:
        # Find the weight adjustment and the new weight of this node
        parent = list(graph.predecessors(unbalanced))[0]
        siblings = list((graph.successors(parent)))
        siblings.remove(unbalanced)
        sibling_weights = Counter([weights[n] for n in siblings])
        diff = weights[unbalanced] - list(sibling_weights)[0]
        print(graph.nodes[unbalanced]['weight'] - diff)
        break

    # Store the total weight of the node
    weights[node] = total
