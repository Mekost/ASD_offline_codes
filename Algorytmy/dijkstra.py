from math import inf
from queue import PriorityQueue

def dijkstra(graph, source):
    n = len(graph)
    parents = [None for _ in range(n)]
    distances = [inf for _ in range(n)]
    distances[source] = 0
    
    queue = PriorityQueue()
    queue.put((0, source))
    
    while not queue.empty():
        vertex = queue.get()[1]
        for neighbour, cost in graph[vertex]:
            if distances[neighbour] > distances[vertex] + cost: # relaxation
                distances[neighbour] = distances[vertex] + cost
                parents[neighbour] = vertex
                queue.put((distances[neighbour], neighbour))
            # if u == destination:
            #     return distances[destination]
    
    return parents, distances
                    
G=[[(1,2),(5,4)],[(0,2),(2,4),(5,1)],[(1,4),(3,1),(5,2)],[(2,1),(4,3)],
[(3,3),(5,1)],[(0,4),(1,1),(2,2),(4,1)]]
print(dijkstra(G,2))
G=[[(1,1),(7,2)],[(0,1),(2,3),(4,3)],[(1,3),(3,5)],[(2,5),(4,2),(6,1)],
[(1,3),(3,2),(5,3),(7,1)],[(4,3),(6,8),(8,1)],[(3,1),(5,8),(8,4)],
[(0,2),(4,1),(8,7)],[(5,1),(6,4),(7,7)]]
print(dijkstra(G,0))