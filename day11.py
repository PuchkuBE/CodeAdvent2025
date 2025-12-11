import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

for line in open('input/day11.txt','r').read().splitlines():
    frm, tos = line.split(": ")
    tos = tos.split(" ")
    G.add_nodes_from([frm]+ tos)
    for to in tos:
        G.add_edge(frm, to)

def searchpath(node , to):
    succ = nx.DiGraph.successors(G, node)  
    nr_paths = 0
    for s in succ:
        if s == to:
            nr_paths += 1
        else:
            nr_paths += searchpath(s, to)
    return nr_paths

print(searchpath('you','out'))