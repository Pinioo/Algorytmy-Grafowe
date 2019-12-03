from dimacs import *
from lab2 import fordFulkerson
import os

def wUndirectedToList(V, E):
    neib = [[] for i in range(V+1)]
    for (u, v, w) in E:
        neib[u].append(v)
        neib[v].append(u)
    return neib

def wUndirectedToMatrix(V, E):
    capacity = [[0 for i in range(V+1)] for i in range(V + 1)]
    for (u, v, w) in E:
        capacity[u][v] = w
        capacity[v][u] = w
    return capacity

def ffConnectivity(V, E):
    s = 1
    minEdges = float('inf')
    for t in range(2, V):
        neib = wUndirectedToList(V, E)
        capacity = wUndirectedToMatrix(V, E)
        minEdges = min(minEdges, fordFulkerson(V, neib, capacity, 1, t))
    return minEdges

directory = "graphs/"
files = ["cycle", "simple", "trivial", "grid5x5", "geo20_2b", "path", "rand100_500"]

for filename in files:
    (V, E) = loadWeightedGraph(os.path.join(directory, filename))
    print("Spójność krawędziowa dla " + filename + ": " + str(ffConnectivity(V, E)))