from egz1Atesty import runtests
from math import inf
from queue import PriorityQueue

def graph_change(G, V, r):
    n = len(G)
    for i in range (n):
       G.append([])
    for vertex in range (n):
        for point in G[vertex]:
          G[vertex + n].append((point[0] + n, 2 * point[1] + r))
        G[vertex].append((vertex + n, (-1) * V[vertex]))
    return G

def relaxation(vertex, neighbour_vertex, distances, neighbour_distance):
    if distances[neighbour_vertex] > distances[vertex] + neighbour_distance:
        distances[neighbour_vertex] = distances[vertex] + neighbour_distance
        return True
    return False

def gold(G,V,s,t,r):
    n = len(G)
    G = graph_change(G, V, r)
    distances = [inf for _ in range (2 * n)]
    distances[s] = 0
    queue = PriorityQueue()
    queue.put((s, 0))
    while not queue.empty():
        vertex, distance = queue.get()
        #print('xd')
        for neighbour_vertex, neighbour_distance in G[vertex]:
            if relaxation(vertex, neighbour_vertex, distances, neighbour_distance):
                queue.put((neighbour_vertex, distances[neighbour_vertex]))
    return min(distances[t], distances[t + n])
        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )

G = [[(1,9), (2,2)], # 0
[(0,9), (3,2), (4,6)], # 1
[(0,2), (3,7), (5,1)], # 2
[(1,2), (2,7), (4,2), (5,3)], # 3
[(1,6), (3,2), (6,1)], # 4
[(2,1), (3,3), (6,8)], # 5
[(4,1), (5,8)] ] # 6
V = [25,30,20,15,5,10,0]
s = 0
t = 6
r = 7
print(gold(G, V, s, t, r))
