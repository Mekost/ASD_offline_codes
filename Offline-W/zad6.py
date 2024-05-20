
# Działanie algorytmu: Na początku przekształcamy graf z postaci macierzowej na postać listy sąsiedztwa.
# Każde pole listy sąsiedztwa jest krotką zawierającą trzy informacje: do jakiego wierzchołka prowadzi krawędź, 
# jaka jest jej długość oraz czy do jej wykonania wymagany jest dwumilowy skok (jump, no_jump).
# W funkcji głównej najpierw zmieniamy dany graf na formę listy sąsiedztwa, a następnie używamy zmodyfikowanego
# algorytmu Dijkstry. Każde pole tablicy distances zawiera dwie komórki, jedna odpowiadająca za poruszanie się bez użycia
# dwumilowych butów, druga - za używanie tychże butów. Idąc dalej w zależności od tego czy mamy dostępny skok 
# zmieniamy odpowiednio wartości w distances i dodajemy kolejne krotki do kolejki. Na sam koniec zwracamy mniejszą wartość
# z distances[w], która jest ostatecznym wynikiem
# Złożoność obliczeniowa: O(EVlogV)

from zad6testy import runtests
from queue import PriorityQueue


def graph_change(G):
    n = len(G)
    new_graph = [[] for _ in range(len(G))]
    for row in range(n - 1):
        for column in range(n):
            if G[row][column] != 0:
                new_graph[row].append((column, G[row][column], 'no_jump'))
                #if column < row: continue
                for i in range(1, n):
                    if i == row: continue
                    if G[column][i] != 0:
                        new_graph[row].append((i, max(G[row][column], G[column][i]), 'jump'))
                        new_graph[i].append((row, max(G[row][column], G[column][i]), 'jump'))
    for j in range(n):
        if G[n - 1][j] != 0:
            new_graph[n - 1].append((j, G[n - 1][j], 'no_jump'))
    return new_graph



def jumper(G, s, w):
    G = graph_change(G)
    n = len(G)
    #print(G)
    def dijkstra_bool(bool):
        distances = [[float('inf'), float('inf')] for _ in range(n)]
        distances[s] = [0, 0]
        Queue = PriorityQueue()
        Queue.put((0, s, bool))
        #print('===========START=========================')
        while Queue.empty() == False:
            distance, vertex, available_jumping = Queue.get()
            #print('from queue:', distance, vertex, available_jumping)
            if vertex == w: return distances[w] if distances[w] != float('inf') else None
            #if distance == distances[vertex][0] or distances[vertex][1]:
            for first, second, jump in G[vertex]:
                #print('from for loop:', first, second, jump)
                if available_jumping == False:
                    if jump == 'jump': continue
                    if distances[first][0] > distance + second:
                        distances[first][0] = distance + second
                        Queue.put((distances[first][0], first, True))
                    #available_jumping = True
                else: 
                    if jump == 'jump':
                        if distances[first][1] > distance + second:
                            distances[first][1] = distance + second
                            Queue.put((distances[first][1], first, False))
                        #available_jumping = False
                    else:
                        if distances[first][0] > distance + second:
                            distances[first][0] = distance + second
                            Queue.put((distances[first][0], first, True))
        return distances[w] if distances[w] != float('inf') else None
    
    result1 = dijkstra_bool(True)
    #result2 = dijkstra_bool(False)
    #print(result1, result2)
    return min(result1[0], result1[1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )