# Wiktor Kostka
# Działanie algorytmu: Na początku tworzymy dwie tablice: w tablicy xsum_list element o indeksie i ma liczbę elementów mniejszych
# lub równych od i z tabeli P (przykład: w tablicy P "0" występuje trzy razy, natomiast "1" cztery razy, więc element na indeksie 1
# w tablicy xsum_list będzie miał wartość 3 + 4 = 7). Tablica ta jest tworzona wyłącznie ze współrzędnych x-owych punktów z tablicy P.
# Tablica ysum_list działa na tej samej zasadzie, tylko jest zrobiona ze współrzędnych y-owych punktów z tablicy P.
# Te tablice tworzymy z pomocą algorytmu QuickSort (wyłącznie pierwszej części, bez samego sortowania)
# Następnie tworzymy pętlę idącą od przez całą tablicę P. Przy każdej iteracji obliczamy sumę ze wzoru xsum_list[x - 1] 
# + ysum_list[y - 1] - n + 1. Maksymalna wartość sum jest wynikiem naszej funkcji i ją zwracamy w ostatecznym rozrachunku
# Złożoność obliczeniowa algorytmu: O(n) 
from zad3testy import runtests

def dominance(P):
    n = len(P)
    xsum_list = countingSort_x(P, n + 1)
    ysum_list = countingSort_y(P, n + 1)
    sum = 0
    summax = 0
    for i in range (0, n):
        sum = xsum_list[P[i][0] - 1] + ysum_list[P[i][1] - 1] - n + 1
        summax = max(sum, summax)
    return summax

def countingSort_x(tab, k):
    n = len(tab)
    temp = [0] * k
    for i in range (n):
        temp[tab[i][0]] += 1
    for j in range (1, k):
        temp[j] += temp[j - 1]
    return temp

def countingSort_y(tab, k):
    n = len(tab)
    temp = [0] * k
    for i in range (n):
        temp[tab[i][1]] += 1
    for j in range (1, k):
        temp[j] += temp[j - 1]
    return temp


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
