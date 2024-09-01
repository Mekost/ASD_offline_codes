from egz1btesty import runtests
from math import inf

# f(i, b) - minimalny koszt znalezienia się na planecie i mając b ton paliwa
# warunek startowy:
# f(0, b) = b * C[0]
# warunek działania funkcji: do dopisania

# złożoność obliczeniowa i pamięciowa: O(n * E)

def planets( D, C, T, E ):
    n = len(D)
    dp_costs = [[inf for _ in range (E + 1)] for _ in range (n)] # tabelka na wyniki dynamika
    dp_costs[T[0][0]][0] = T[0][1] # dodajemy do tabelki teleport z planety A (zerowej)
    for starting in range (E + 1):
        dp_costs[0][starting] = starting * C[0] # zaczynając możemy tankować tylko na pierwszej planecie, więc pierwszy "wiersz" tabelki z wynikami zawiera tylko możliwości tankowania na planecie A
    #print(dp_costs)
    for current_planet in range (1, n): # zaczynamy od planety z indeksem 1, bo ta z indeksem 0 jest już rozpatrzona
        for fuel_amount in range (E + 1):
            if E - (D[current_planet] - D[current_planet - 1]) - fuel_amount + 1 > 0:
                dp_costs[current_planet][fuel_amount] = min(dp_costs[current_planet][fuel_amount], dp_costs[current_planet - 1][fuel_amount + (D[current_planet] - D[current_planet - 1])])
                # jeżeli po przejściu z planety na planetę mogło nam zostać jeszcze trochę paliwa (przy założeniu że np. bak statku jest pełen)
                # to możemy wtedy sprawdzić, czy nie będzie taniej nalać więcej paliwa na poprzedniej planecie zamiast kupować droższe na aktualnej
                # (wiadomo że jak np. rozmiar baku to 10 i odległość między planetami to też 10, to nie ma możliwości żeby nalać sobie na zapas)
            dp_costs[current_planet][fuel_amount] = min(dp_costs[current_planet][fuel_amount], dp_costs[current_planet][fuel_amount - 1] + C[current_planet])
            # jednocześnie rozpatrujemy możliwość kupowania paliwa na aktualnej planecie (tu nie ma warunku, bo zawsze mamy taką możliwość)
        #print(dp_costs)
        tp_location, tp_cost = T[current_planet]
        if tp_location != current_planet:
            dp_costs[tp_location][0] = min(dp_costs[tp_location][0], dp_costs[current_planet][0] + tp_cost)
        # sprawdzamy czy teleport na aktualnej planecie działa, jeżeli tak, to aktualizujemy tabelkę z wynikami o potencjalny teleport na którąś z następnych planet
    #print(dp_costs)  
    return min(dp_costs[n - 1]) # chcemy się dostać na planetę z indeksem n - 1, więc wynikiem algorytmu będzie najmniejszy z kosztów dostania się na n - 1 planetę (znając życie będzie to przy pustym baku xd)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

# 0 1 2 3
# D = [ 0, 5, 10, 20]
# C = [ 2, 1, 3, 9]
# T = [(2,3), (3,7), (2,10), (3,10)]
# E = 10

# D = [0, 1, 4, 6, 7, 10, 11, 12, 13, 15, 16]
# C = [2, 6, 2, 10, 2, 10, 4, 6, 8, 8, 4]
# T = [(0, 0), (5, 8), (2, 0), (7, 10), (10, 6), (10, 26), (10, 6), (10, 2), (8, 0), (9, 0), (10, 2)]
# E = 5
# #Prawidlowy wynik :  20
# #Wynik algorytmu  :  26
# print(planets(D, C, T, E))
