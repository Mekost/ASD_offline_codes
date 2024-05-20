# Wiktor Kostka
# W algorytmie zastosowano insertion sort dostosowany do potrzeb polecenia. Algorytm polega na tym, że na początku tworzymy pętlę
# idącą przez każdy element listy odsyłaczowej. Przy każdej iteracji pętli jako zmienną nodetochange oznaczamy aktualny Node, na
# którym znajduje się pętla, do zmiennej lowestnode natomiast mamy na celu przypisać Node'a o najmniejszej wartości spośród 
# najbliższych k możliwych. Po k iteracjach pętli wewnętrznej (lub jeżeli lista się skończy) zamieniamy ze sobą wartości 
# nodetochange oraz lowestnode. Na koniec zwracamy odsyłacz wskazujący na początek listy odsyłaczowej
# Złożoność algorytmu: O(n*k) (przejście przez pętlę o długości n, przy każdej iteracji sprawdzenie do k elementów)
# Złożoności czasowe dla:
# > k = Θ(1): O(n)
# > k = Θ(log n): O(n* log n)
# > k = Θ(n): O(n^2)
from zad1testy import Node, runtests

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


def SortH(p,k):
    begin = p
    first = p
    while first != None:
        nodetochange = first
        lowestnode = first
        k_repeat = 0
        p = first.next
        while p != None and k_repeat < k:
            if p.val < lowestnode.val:
                lowestnode = p
            p = p.next
            k_repeat += 1
        nodetochange.val, lowestnode.val = lowestnode.val, nodetochange.val
        first = first.next
    return begin

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
