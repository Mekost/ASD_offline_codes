
# Działanie: Docelowo algorytm robi tylko jedno sortowanie na początku, po czym przy każdej iteracji pętli wykonującej się n-p razy
# wyrzuca z tablicy pomocniczej element o najmniejszym indeksie z oryginalnej tablicy i dodaje w odpowiednie miejsce kolejny element,
# przy każdej iteracji pętli dodając do sumy wartość k-tego największego elementu z danej tablicy
# Na początku tworzymy pomocniczą tablicę temp, która przed wejściem do pętli zawiera pierwszych p elementów z tablicy T.
# Następnie sortujemy tą tablicę za pomocą HeapSortu, po czym ją odwracamy
# Przy każdej iteracji pętli wykonujemy trzy operacje:
# 1) Dodajemy do zmiennej sum wartość k-tego największego elementu z tablicy temp (dla tablicy posortowanej nierosnąco k-ty największy
# element stoi na pozycji k-1)
# 2) Usuwamy z tablicy temp element, który w tablicy T ma najmniejszy indeks (do usuwania elementu używamy funkcji .pop, natomiast
# samego indeksu tego elementu szukamy przez zmodyfikowanego BinarySearcha)
# 3) Wstawiamy to tablicy temp następny w kolejności element z tablicy T w odpowiednie miejsce tak, aby tablica temp była wciąż
# posortowana (.insert odpowiada za włożenie elementu w odpowiednie miejsce, BinarySearch szuka nam indeksu, w który trzeba dać element)
# Na koniec działania funkcji zwracamy zmienną sum
# Złożoność obliczeniowa programu: Θ(n * p) (średnia)
from zad2testy import runtests
def ksum(T, k, p):
    n = len(T)
    sum = 0
    temp = T[0:p] # na start naszą tablicę temp tworzy p pierwszych elementów
    heap_sort(temp) # sortujemy p-elementową tablicę HeapSortem
    temp = temp[::-1]
    for i in range (0, n - p):
        sum += temp[k - 1] # dodajemy do sumy k-ty największy element z tabeli tymczasowej
        temp.pop(binary_search(temp, T[i])) # usuwamy element, który ma najmniejszy indeks w tablicy T
        temp.insert(binary_search(temp, T[p + i]), T[p + i]) # wstawiamy do tablicy temp kolejny element z tablicy T w odpowiednie miejsce 
    sum += temp[k - 1]
    return sum

def binary_search(T, a): # dostosowany do tablicy posortowanej nierosnąco
    left = 0
    right = len(T) - 1
    while left < right:
        middle = (left + right) // 2
        if T[middle] == a: return middle
        elif T[middle] > a:
            left = middle + 1
        else:
            right = middle
    return right

# Funkcje do HeapSorta:

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i - 1) // 2

def heapify(T, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, n, max_ind)

def build_heap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)

def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )