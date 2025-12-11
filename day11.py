import networkx as nx

G = nx.DiGraph()

for line in open('input/day11.txt','r').read().splitlines():
    frm, tos = line.split(": ")
    tos = tos.split(" ")
    G.add_nodes_from([frm]+ tos)
    for to in tos:
        G.add_edge(frm, to)

def searchpath(node , to, fft, dac, cache: set):
    succ = nx.DiGraph.successors(G, node)  
    nr_paths = 0
    if (node, fft, dac) in cache:
        return cache[(node, fft, dac)]
    fft = fft or node == 'fft'
    dac = dac or node == 'dac'
    for s in succ:
        if s == to and fft and dac:
            nr_paths += 1
        else:
            nr_paths += searchpath(s, to, fft, dac, cache)
    cache[(node, fft, dac)] = nr_paths            
    return nr_paths

print(f'Solution for day11/part1: {searchpath('you','out',True, True, {})}')
print(f'Solution for day11/part2: {searchpath('svr','out', False, False, {})}')