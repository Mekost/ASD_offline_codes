from zad6testy import runtests
from queue import PriorityQueue
from math import inf

def jumper( G, s, w ):
    for y in range(len(G)):
        for x in range(len(G)):
            if G[y][x][0] != 0:
                for i in range(len(G)):
                    if G[G[y][x]][i][0] != G[y][x][0] and G[G[y][x]][i][0] < G[y][i][1]:
                        G[y][i][1] = 
    
    return None

def Dijkstra_list(G, s):
    distance = [ inf for _ in range(len(G)) ]
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    distance[s] = 0
    PQ = PriorityQueue()
    PQ.put((0, s))

    while not PQ.empty():
        current_distance, vertex = PQ.get()
        visited[vertex] = True
        if current_distance > distance[vertex]:
            continue

        for neighbour, weight in G[vertex]:
            dist = current_distance + weight

            if dist < distance[neighbour] and not visited[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                PQ.put((dist, neighbour))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = False )