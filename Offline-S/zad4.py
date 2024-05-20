
# Algorytm opiera sie na zmodyfikowanym dfsie. Na poczatku zamienia graf na wygodniejsza postac list sasiedztwa,
# gdzie sasiadujacy wierzcholek jest pierwszym elementem krotki a pulap drugim. Funkcja dfsVisit rekurencyjnie
# zapisuje odwiedzone juz wierzcholki i ich pulapy


from zad4testy import runtests

def Flight(L,x,y,t):
    def dfsVisit(graph, u, visited, heights):
        if u == y:
            return True
        for v in graph[u]:
            if v[0] not in visited:
                temp = heights+[v[1]]
                if max(temp) - min(temp) <= 2*t:
                    if dfsVisit(graph, v[0], visited+[v[0]], heights+[v[1]]):
                        return True
        return False

    return dfsVisit(change(L), x, [x], [])

def change(L): # funkcja zamieniajaca graf na liste sasiedztwa
    max_v = 0
    for v in L:
        max_v = max(max_v, v[0], v[1])
        
    graph = [[] for _ in range(max_v+1)]
    for v in L:
        graph[v[0]].append((v[1],v[2]))
        graph[v[1]].append((v[0],v[2]))
    return graph

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
