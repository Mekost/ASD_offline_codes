from queue import Queue

def bfs(graph, s):
    n = len(graph)
    visited = [False for v in range(n)]
    distance = [-1 for v in range(n)]
    parent = [None for v in range(n)]
    queue = Queue()
    
    visited[s] = True
    distance[s] = 0
    queue.put(s)
    
    while not queue.empty():
        vertex = queue.get()
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                parent[neighbour] = vertex
                distance[neighbour] = distance[vertex] + 1
                queue.put(neighbour)
    return visited, parent, distance

graph = [[1],[2],[3,4],[2,4,5],[2,3],[3]]
print(bfs(graph, 0))