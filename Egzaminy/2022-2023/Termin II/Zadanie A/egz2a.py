from egz2atesty import runtests

# najgłupszy brut świata, złożoność O(n^2), 2 pkt (!!!) za złożoność (XD)
# def dominance(P):
#     n = len(P)
#     most_dominant = 0
#     for i in range (n):
#         temp_dominant = 0
#         for j in range (n):
#             if i == j: continue
#             if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
#                 temp_dominant += 1
#         most_dominant = max(most_dominant, temp_dominant)
#     return most_dominant

# rozwiązanie "ambitniejsze", używa counting sorta (przynajmniej częściowo)
# najpierw tworzymy tablice x_table i y_table, w których będziemy przechowywać nasze obliczenia
# tablice te będą działały na wzór tej z counting sorta: przykładowo dla x_table, 
# komórka x_table[i] będzie zawierała ilość współrzędnych "x" z tablicy P, które mają wartość mniejszą lub równą i
# (analogicznie działa tablica y_table)
# formuła na ilość dominowanych punktów: x_table[x - 1] + y_table[y - 1] - n + 1
# Złożoność obliczeniowa: O(n)

def dominance(P):
    n = len(P)
    x_table = [0 for _ in range (n + 1)]
    y_table = [0 for _ in range (n + 1)]
    # wartości x i y zawierają się w przedziale 0...n
    for x, y in P:
        x_table[x] += 1
        y_table[y] += 1
    for i in range (1, n + 1):
        x_table[i] += x_table[i - 1]
        y_table[i] += y_table[i - 1]
    result = 0
    for x, y in P:
        temp = x_table[x - 1] + y_table[y - 1] - n + 1
        # skoro x_table[x] zawiera wsp. x mniejsze lub równe x, to x_table[x - 1] będzie zawierało tylko wsp. mniejsze od x
        # analog. z y_table
        result = max(result, temp)
    return result





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

P = [(1,3),
(3,4),
(4,2),
(2,2)]

print(dominance(P))
