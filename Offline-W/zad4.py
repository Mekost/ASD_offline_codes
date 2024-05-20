
# Działanie algorytmu: Na początku zamieniamy daną w zadaniu listę na listę sąsiedztwa zawierającą przy okazji pułapy przy odpowiednich
# wierzchołkach. Następnie definiujemy zmienne maxival i minival, które będą przechowywały odpowiednio największy i najmniejszy z pułapów
# na danej trasie. Potem tworzymy rekurencyjną funkcję dfs_visit, którą będziemy sprawdzali, czy zadana trasa istnieje. Na początku
# funkcji sprawdzamy warunek maxival - minival > 2*t, który zarówno wykluczy wszystkie niepoprawne trasy, jak i jest koniecznym
# warunkiem naszej szukanej trasy. Jeżeli warunek jest spełniony, ale jeszcze nie znaleźliśmy zadanej trasy szukamy dalej idąc przez
# kolejne krawędzie połączone z naszym wierzchołkiem. W momencie gdy w wyniku rekurencji poszliśmy w złą stronę, stosujemy tzw. 
# backtracking i szukamy dalej odpowiedniej ścieżki. Jeżeli algorytm przejdzie wszystkie możliwe ścieżki i nie znajdzie trasy
# spełniającej warunki zadania, zwracane jest False
# Złożoność czasowa algorytmu: O(V^2)
from zad4testy import runtests

def list_change(L):
    new_list = [[] for _ in range (len(L))]
    for p in L:
        new_list[p[0]].append((p[1], p[2]))
        new_list[p[1]].append((p[0], p[2]))
    while new_list[len(new_list) - 1] == []:
        new_list.pop()
    return new_list

def Flight(L,x,y,t):
        L = list_change(L)
        n = len(L)
        print(n)
        visited = [False] * n
        maxival = float('-inf')
        minival = float('inf')
        def dfs_visit(v):
            nonlocal visited, maxival, minival
            if maxival - minival > 2 * t: return False
            if v == y:
                 return True
            visited[v] = True
            for i in L[v]:
                temp = i[0]
                if visited[temp] == False:
                    prevmaxi = maxival
                    maxival = max(maxival, i[1])
                    prevmini = minival
                    minival = min(minival, i[1])
                    if dfs_visit(temp) == True: return True
                    maxival = prevmaxi
                    minival = prevmini
            visited[v] = False        
            return False
        return dfs_visit(x)



    



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
