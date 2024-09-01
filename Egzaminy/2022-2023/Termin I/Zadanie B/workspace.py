from egz1btesty import runtests
from math import inf

# f(i, b) - minimalny koszt znalezienia się na planecie i mając b ton paliwa
# warunek startowy:
# f(0, b) = b * C[0]

def planets( D, C, T, E ):
    n = len(D)
    dp_costs = [[inf for _ in range (E + 1)] for _ in range (n)]
    for starting in range (E + 1):
        dp_costs[0][starting] = starting * C[0]
    #print(dp_costs)
    for current_planet in range (1, n):
        # if dp_costs[current_planet][0] != inf:
        #     if dp_costs[current_planet][0] < dp_costs[current_planet - 1][(D[current_planet] - D[current_planet - 1])]:
        #         for fuel_amount in range (1, E + 1):
                    
        for fuel_amount in range (E + 1):
                if C[current_planet] > C[current_planet - 1]:
                    if E - (D[current_planet] - D[current_planet - 1]) - fuel_amount >= 0:
                        if fuel_amount == 0: dp_costs[current_planet][fuel_amount] = min(dp_costs[current_planet - 1][(D[current_planet] - D[current_planet - 1])], dp_costs[current_planet][fuel_amount])
                        else: dp_costs[current_planet][fuel_amount] = dp_costs[current_planet][fuel_amount - 1] + C[current_planet - 1]
                    else:
                        dp_costs[current_planet][fuel_amount] = dp_costs[current_planet][fuel_amount - 1] + C[current_planet]
                else:
                    if fuel_amount == 0: dp_costs[current_planet][fuel_amount] = min(dp_costs[current_planet - 1][(D[current_planet] - D[current_planet - 1])], dp_costs[current_planet][fuel_amount])
                    else: dp_costs[current_planet][fuel_amount] = dp_costs[current_planet][fuel_amount - 1] + C[current_planet]
        #print(dp_costs)
        tp_location, tp_cost = T[current_planet]
        if tp_location != current_planet:
            dp_costs[tp_location][0] = dp_costs[current_planet][0] + tp_cost
    #print(dp_costs)  
    return min(dp_costs[n - 1])

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
