def dfs(graph, source):
    def dfsVisit(graph, vertex):
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                parent[neighbour] = vertex
                dfsVisit(graph, neighbour)

    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    
    dfsVisit(graph, source)
    return visited, parent
    
graph = [[1],[2],[3,4],[2,4,5],[2,3],[3]]
print(dfs(graph, 0))