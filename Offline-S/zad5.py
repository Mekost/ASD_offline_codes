
# Algorytm najpierw zamienia graf z zadania na postac list sasiedztwa (A), nastepnie dodaje do kazdego wierzcholka z osobliwosci
# droge do wszystkich innych wierzcholkow z osobliwosci (dodaje krawedz z kosztem przelotu 0) (B) i na koncu wlacza zwyklego Dijkstre
# na utworzonym grafie (C)

from zad5testy import runtests
from queue import PriorityQueue
from math import inf

def spacetravel( n, E, S, a, b ):
    graph = change(E, n) # (A)
    for u in range(len(S)-1): # (B)
        for v in range(u+1, len(S)):
            graph[S[u]].append((S[v], 0))
            graph[S[v]].append((S[u], 0))    
    return dijkstra(graph, a, b) # (C)

def change(E, n):
    graph = [[] for _ in range(n)]
    for u, v, cost in E:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    return graph

def dijkstra(graph, source, destination):
    n = len(graph)
    distances = [inf for _ in range(n)]
    distances[source] = 0
    
    queue = PriorityQueue()
    queue.put((0, source))
    
    while not queue.empty():
        u = queue.get()[1] # "trik" z bitu :D
        for v, cost in graph[u]:
            if distances[v] > distances[u] + cost: # relaksacja
                distances[v] = distances[u] + cost
                queue.put((distances[v], v))
            if u == destination:
                return distances[destination]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )