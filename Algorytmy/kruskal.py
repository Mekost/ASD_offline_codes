import unittest

# gemini
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > y_root:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskalMst(edges):
    num_nodes = 0
    for u, v, weight in edges:
        num_nodes = max(u, v, num_nodes)
    num_nodes += 1
    
    mst = []
    edges.sort(key=lambda x: x[2])

    parent = list(range(num_nodes))
    rank = [0] * num_nodes

    for u, v, weight in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append((u, v, weight))
            union(parent, rank, x, y)

    return mst


# git
class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def Find(x):
    if x.parent != x:
        x.parent = Find( x.parent )
    return x.parent

def Union(X, Y): # X - root, Y - root 
    if X.rank > Y.rank:
        Y.parent = X
    elif X.rank < Y.rank:
        X.parent = Y
    else:
        X.parent = Y 
        Y.rank += 1

def sortEdges(E):
    E.sort( key = lambda x: x[2] )
    return E

def Kruskal(G):
    V, E = G
    minSpanningTree = []
    E = sortEdges(E)
    Vertices = [ Node(v) for v in V ]
    
    for edge in E:
        a, b, weight = edge
        rootA, rootB = Find( Vertices[a] ), Find( Vertices[b] )
        if rootA != rootB:
            Union( rootA, rootB )
            minSpanningTree.append( edge )
    return minSpanningTree

def createG(E):
    # This function creates an array of vertices based on the array of edges
    # and returns both, array of vertices and array of edges
    return list(set(map(lambda e: e[0], E)) | set(map(lambda e: e[1], E))), E

edges1 = [
    (0, 1, 2), (0, 2, 3), 
    (1, 0, 2), (1, 2, 1), (1, 3, 1),
    (2, 0, 3), (2, 1, 1), (2, 3, 4),
    (3, 1, 1), (3, 2, 4)]

edges2 = [(5, 0, 2), (0, 1, 3), (1, 2, 1), (5, 6, 1), (1, 6, 2), (5, 4, 6),
            (4, 3, 8), (3, 6, 5), (2, 3, 7)]

edges3 = [(0, 5, 1), (0, 1, 2), (1, 2, 7), (5, 6, 3), (6, 1, 8), (5, 4, 2), (4, 6, 5),
            (4, 3, 6), (3, 2, 4)]

edges4 = [(0, 1, 7), (1, 2, 1), (2, 3, 12), (3, 4, 6), (4, 5, 5), (0, 5, 2), (0, 3, 3),
            (0, 2, 8), (2, 4, 4)]

graphs = [edges1, edges2, edges3, edges4]
for graph in graphs:
    print(kruskalMst(graph) == Kruskal(createG(graph)))