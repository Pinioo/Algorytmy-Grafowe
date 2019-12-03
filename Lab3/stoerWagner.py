from dimacs import loadWeightedGraph
from queue import PriorityQueue
import os

class Node:
    def __init__(self):
        self.edges = {}    # słownik par mapujący wierzchołki do których są krawędzie na ich wagi
        self.deleted = False

    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                    # o zadanej wadze; a jeśli taka krawędź
                                                    # istnieje, to dodaj do niej wagę
    def delEdge(self, to ):
        del self.edges[to]                              # usuń krawędź do zadanego wierzchołka

def mergeVertices(G, x, y):
    for (u, w) in list(G[y].edges.items()):
        G[y].delEdge(u)
        G[u].delEdge(y)
        if u != x:
            G[x].addEdge(u, w)
            G[u].addEdge(x, w)

def minimumCutPhase(G, V):
    visited = [False for _ in range(V+1)]
    weights = [0 for _ in range(V+1)]

    Q = PriorityQueue()
    Q.put((0, 1))

    S = []

    while not Q.empty():
        (w, v) = Q.get()
        w = -w

        if not visited[v]:
            visited[v] = True
            S.append(v)
            for (u, w) in G[v].edges.items():
                if not visited[u]:
                    weights[u] += w
                    Q.put((-weights[u], u))

    s = S[-1]
    t = S[-2]

    toReturn = 0
    for w in G[s].edges.values():
        toReturn += w

    mergeVertices(G, s, t)
    return toReturn

def stoerWagner(V, E):
    G = [Node() for _ in range(V+1)]

    for (x,y,c) in E:
        G[x].addEdge(y,c)
        G[y].addEdge(x,c)

    activeVertices = V
    result = float('inf')
    while activeVertices > 1:
        result = min(result, minimumCutPhase(G, V))
        activeVertices -= 1

    return result

def run(file):
    (V, E) = loadWeightedGraph(file)
    return stoerWagner(V, E)

grDir = "graphs"
for f in os.listdir(grDir):
    if f == "grid100x100":
        continue
    print("Result for {}: {}".format(f, run(os.path.join(grDir, f))))