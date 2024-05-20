
# Algorytm dziala podobnie do sortowania przez wstawianie. Roznica jest taka, ze porownujemy klucz z k nastepnymi elementami aby
# znalezc najmniejsza wartosc i nastepnie zamieniamy klucz z ta najmniejsza wartoscia (chyba ze klucz jest najmniejszy).
# Algorytm dziala poniewaz z tresci wiemy, ze wsrod k pierwszych elementow listy jest wartosc ktora powinna byc pierwsza
# i analogicznie po i-tym wykonaniu glownej petli, i elementow listy bedzie posortowane.
# zlozonosc dla k=O(1) to O(n), dla k=O(logn) to O(nlogn), dla k=O(n) to O(nlogn)

from zad1testy import Node, runtests
import time

class Node:
    def __init__(self):
        self.val = None # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    prev_current = Node() # tworze guardiana, poniewaz przy iterowaniu przez liste bede "trzymal" element poprzedzajacy ten, ktory aktualnie sprawdzam
    head = prev_current # zapisuje poczatek listy, poniewaz jesli pierwszy element nie jest najmniejszy to zgubie poczatek lsity
    prev_current.next = p # podpinam do wartownika liste wyslana przez uzytkownika
    while prev_current.next != None: # glowna petla
        temp = prev_current.next # tymczasowa zmienna ktora sluzy do znalezienia najmniejszej z k kolejnych wartosci (do przeiterowania przez k kolejnych elementow)
        prev_mini = prev_current.next
        mini = prev_current.next
        for _ in range(k): # petla szukajaca najmniejszej wartosci wsrod k nastepnych elementow po prev_current.next
            if temp.next != None:
                if temp.next.val < mini.val:
                    prev_mini = temp
                    mini = temp.next
                temp = temp.next
            else:
                break # break nie jest "ladny" ale usprawni dzialanie programu dla koncowych elementow listy
        if mini != prev_current.next: # jesli wartosc najmniejsza nie jest juz na swoim miejscu, to zamieniamy z nia (z mini) prev_current.next
            swapNodes(prev_current, prev_mini)
        prev_current = prev_current.next
    return head.next
    # pass

def swapNodes(prev_a, prev_b):
    prev_a.next, prev_b.next = prev_b.next, prev_a.next
    prev_a.next.next, prev_b.next.next = prev_b.next.next, prev_a.next.next

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
