from lexBFS import *


class HelperNode:
    def __init__(self, index):
        self.vertex = index
        self.children = []


class CliqueNode:
    def __init__(self):
        self.vertices = set()
        self.children = []


def buildHelperTree(G, V, firstVertex, rn):
    root = HelperNode(firstVertex)
    currentNode = root
    used = 1
    while used < V:
        for tmp in enumerate(rn):
            if rn and rn[-1]:


def buildCliqueTree(G, V):
    lex = lexBFS(G, V)
    c = [None for _ in range(V+1)]
    rn = [[] for _ in range(V+1)]
    for (i, v) in enumerate(lex):
        for prev in lex[:i-1]:
            if prev in G[v].out:
                rn[v].append(prev)
    root = CliqueNode()
    root.vertices.add(lex[0])
