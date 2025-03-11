from zad9testy import runtests
from collections import deque

def graph_change(M):
  rows = len(M)
  columns = len(M[0])
  #print(rows, columns)
  new_graph = [[] for _ in range (rows * columns)]
  #print(rows, columns)
  x = 0
  for i in range (rows):
    for j in range (columns):
      #print(M[i][j])
      if j + 1 < columns and M[i][j + 1] > M[i][j]:
        new_graph[x].append(x + 1)
      if i + 1 < rows and M[i + 1][j] > M[i][j]:
        new_graph[x].append(x + columns)
      if i - 1 >= 0 and M[i - 1][j] > M[i][j]:
        new_graph[x].append(x - columns)
      if j - 1 >= 0 and M[i][j - 1] > M[i][j]:
        new_graph[x].append(x - 1)
      x += 1
  return new_graph

def DFS(G, path, visited, v):

    visited[v] = True 

    for vertex in G[v]:
        if visited[vertex] == False:
            path = DFS(G, path, visited, vertex)
    path.appendleft(v)
    return path


def topo_sort(G):
    n = len(G)
    visited = [ False for _ in range(n) ]
    path = deque()

    for v in range(n):
        if visited[v] == False:
            path = DFS(G, path, visited, v)
    #
    return path


def trip(M):
  M = graph_change(M)
  path_topo = topo_sort(M)
  n = len(M)
  #print(M)
  F = [1 for _ in range (n)]
  visited = [False for _ in range (n)]
  result = 0
  def inner_dfs(vertex):
    visited[vertex] = True
    for x in M[vertex]:
      if not visited[x]:
          inner_dfs(x)
      F[vertex] = max(F[vertex], F[x] + 1)

  for x in path_topo:
    if not visited[x]:
      inner_dfs(x)
    result = max(result, F[x])
  
  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
