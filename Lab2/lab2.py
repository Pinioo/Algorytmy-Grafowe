from dimacs import *
import os

def BFS(V, neib, capacity, s, t, parent):
    visited = [False for i in range(V+1)]
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for v in neib[u]:
            if visited[v] == False and capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[t]

def findFlowOnPath(capacity, s, t, parent):
    tmp = parent[t]
    maxFlow = capacity[tmp][t]
    while tmp != s:
        maxFlow = min(maxFlow, capacity[parent[tmp]][tmp])
        tmp = parent[tmp]
    return maxFlow

def updateResidual(capacity, maxFlow, s, t, parent):
    tmp = t
    while tmp != s:
        capacity[parent[tmp]][tmp] -= maxFlow
        capacity[tmp][parent[tmp]] += maxFlow
        tmp = parent[tmp]

def toListRep(V, E):
    neib = [[] for i in range(V+1)]
    for (u, v, w) in E:
        neib[u].append(v)
    return neib

def toMatrixRep(V, E):
    capacity = [[0 for i in range(V+1)] for j in range(V+1)]
    for (u, v, w) in E:
        capacity[u][v] = w
    return capacity

def fordFulkerson(name):
    (V, E) = loadDirectedWeightedGraph(name)

    s = 1
    t = V
    neib = toListRep(V, E)
    capacity = toMatrixRep(V, E)
    for i in range(1, V):
        for v in neib[i]:
            if capacity[v][i] == 0:
                neib[v].append(i)

    parent = [-1 for i in range(V+1)]
    flow = 0

    while BFS(V, neib, capacity, s, t, parent):
        flowOnPath = findFlowOnPath(capacity, s, t, parent)
        updateResidual(capacity, flowOnPath, s, t, parent)
        flow += flowOnPath

    return flow

directory = "graphs/flow"
for filename in os.listdir(directory):
    print("Maks. przepływ dla " + filename + " = " + str(fordFulkerson(os.path.join(directory, filename))))



