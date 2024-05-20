# Wiktor Kostka
# Działanie algorytmu: Na początku zmieniamy postać grafu na listę sąsiedztwa w celu bardziej intuicyjnego działania na grafie.
# Potem tworzymy nowe krawędzie między wierzchołkami koło osobliwości, których długość wynosi 0.
# Następnie tworzymy algorytm Dijkstry (tworzymy kolejkę priorytetową, tworzymy tablicę distances gdzie każdy dystans wynosi
# niesk. na początku, tworzymy charakterystyczną dla algorytmu funkcje relaxation itp.)
# Na końcu zwracamy najkrótszą odległość od a do b, czyli distances[b] (jeżeli odległość na końcu działania programu wynosi inf,
# to znaczy że trasa jest niemożliwa do zrealizowania, więc zwracamy None)
# Złożoność algorytmu: O(len(S)^2 + E log V) 

from zad5testy import runtests

from queue import PriorityQueue

def graph_change(E, n):
    new_graph = [[] for _ in range (n)]
    for path in E:
        new_graph[path[0]].append((path[1], path[2]))
        new_graph[path[1]].append((path[0], path[2]))
    return new_graph

def spacetravel(n, E, S, a, b):
    E = graph_change(E, n)
    for i in S:
        for j in S:
            if i == j: continue
            E[i].append((j, 0))
    distances = [float('inf') for _ in range(n)]
    distances[a] = 0
    Queue = PriorityQueue()
    Queue.put((0, a))
    while Queue.empty() == False:
        distance, vertex = Queue.get()
        if distance == distances[vertex]:
            for first, second in E[vertex]:
                if relaxation(distances, first, second, vertex):
                    Queue.put((distances[first], first))
    return distances[b] if distances[b] != float('inf') else None

def relaxation(distances, first, second, d):
    if distances[first] > distances[d] + second:
        distances[first] = distances[d] + second
        return True
    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )