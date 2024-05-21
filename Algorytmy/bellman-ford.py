from math import inf

def bellmanFord(graph, source, destination=None):
    n = len(graph)
    distances = [inf for _ in range(n)]
    parents = [False for _ in range(n)]
    distances[source] = 0
    
    for _ in range(n-1):
        for vertex in range(n):
            for neighbour, weight in graph[vertex]:
                if distances[neighbour] > distances[vertex] + weight:
                    distances[neighbour] = distances[vertex] + weight
                    parents[neighbour] = vertex
    
    for _ in range(n-1):
        for vertex in range(n):
            for neighbour, weight in graph[vertex]:
                if distances[neighbour] > distances[vertex] + weight:
                    distances[neighbour] = -inf # cykl ujemny

    if destination != None:
        path = []
        vertex = destination
        while vertex != None:
            path.append(vertex)
            vertex = parents[vertex]
        return path[::-1]

    return distances

def createGDirected(edges):
    n = 0
    for edge in edges:
        n = max( n, edge[0], edge[1] )
    #
    G = [ [] for _ in range(n+1) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a].append( (b, weight) )
    #
    return G


E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]
s = 0

G = createGDirected(E)
print( bellmanFord(G, s) )