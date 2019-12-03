from dimacs import loadWeightedGraph
import os

class Node:
  def __init__(self, idx):
    self.idx = idx
    self.out = set()

  def connect_to(self, v):
    self.out.add(v)


def lexBFS(G, V):
    setsList = [{i for i in range(2, V+1)}, {1}]
    resultStack = []
    notNeibours = set()
    neibours = set()

    while setsList:
        lastSet = setsList[-1]
        v = lastSet.pop()
        resultStack.append(v)
        newSetsList = []
        for s in setsList:
            notNeibours = set()
            neibours = set()
            for u in s:
                if u in G[v].out:
                    neibours.add(u)
                else:
                    notNeibours.add(u)
            if notNeibours:
                newSetsList.append(notNeibours)
            if neibours:
                newSetsList.append(neibours)
        setsList = newSetsList
    return resultStack


def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
    return True


grDir = "graphs/chordal"

for f in os.listdir(grDir):
    (V, L) = loadWeightedGraph(os.path.join(grDir, f))
    G = [None] + [Node(i) for i in range(1, V + 1)]
    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    print("{}: {}".format(f, checkLexBFS(G, lexBFS(G, V))))
"""

(V, L) = loadWeightedGraph(os.path.join(grDir, "interval-rnd10"))
G = [None] + [Node(i) for i in range(1, V + 1)]
for (u, v, _) in L:
    G[u].connect_to(v)
    G[v].connect_to(u)
print(checkLexBFS(G, lexBFS(G, V)))

"""
