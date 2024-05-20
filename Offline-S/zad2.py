
# Algorytm iteruje przez elementy 0, n-p tablicy podanej w zadaniu. Glownym pomyslem algorytmu jest utworzenie tablicy pomocniczej, ktora przechowuje elementy i, i+p-1 i jest
# zawsze posortowana. W kazdej iteracji usunieta zostaje poprzednia wartosc (i-1), ktora juz nie nalezy do przedzialu i, i+p-1 i dodana zostaje nowa (i+p-1). Oczywiscie
# operacje te zachowuja kolejnosc niemalejaca w tablicy pomocniczej. Do dodawania elementow korzystam z binarySearcha, ktory ma zlozonos O(logn) w najgorszym wypadku
# a w najlepszym O(1). .pop i .insert maja zlozonosc O(n) w najgorszym wypadku. 
# Zlozonosc algorytmu to O(nplogp) w najgorszym wypadku

from zad2testy import runtests

def ksum(T, k, p):
    sum = 0
    tab = T[:p] # tworze tablice pomocnicza, ktora zawsze bedzie posortowana, na poczatku sklada sie ona z elementow o indeksach (dla tablicy T) 0 do p-1 wlacznie
    heapSort(tab)
    sum += tab[-k] # przez to ze tablica jest posortowana tab[-k] to zawsze bedzie k-ta najwieksza wartosc rozwazanego przedzialu
    for i in range(1, len(T)-p+1): # glowna petla, ktora policzy z_0+z_1+...z_(n-p)
        tab.pop(binarySearch(tab, T[i-1])) # binarySearch szuka indeksu poprzedniego elementu i (elementu dla ktorego szukamy z_i) w tablicy pomocniczej tab a nastepnie usuwa go z niej
        tab.insert(binarySearch(tab, T[i+p-1]), T[i+p-1]) # binarySearch szuka (indeksu) gdzie wstawic nowy element do tablicy pomocniczej
        sum += tab[-k]
    return sum

def binarySearch(tab, x): # klasyczny binary search, jezeli element nie istnieje to zwroci indeks w ktorym powinien sie znalezc
    left = 0
    right = len(tab)-1
    while left <= right:
        mid = left + (right - left) // 2
        if tab[mid] == x:
            return mid
        elif tab[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

def maxHeapify(tab, n, i):
    l = 2*i + 1
    r = 2*i + 2
    max = i
    if l < n and tab[l] > tab[max]:
        max = l
    if r < n and tab[r] > tab[max]:
        max = r
    if max != i:
        tab[i], tab[max] = tab[max], tab[i]
        maxHeapify(tab, n, max)

def builMaxHeap(tab):
    n = len(tab)
    for i in range((n-2)//2, -1, -1):
        maxHeapify(tab, n, i)

def heapSort(tab):
    n = len(tab)
    builMaxHeap(tab)
    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        maxHeapify(tab, i, 0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )