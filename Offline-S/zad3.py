from zad3testy import runtests

def dominance(P):
    n = len(P)
    xsum_list = countingSort(P, n+1, 0)
    ysum_list = countingSort(P, n+1, 1)
    sum = 0
    sum_max = 0
    for i in range(0, n):
        sum = xsum_list[P[i][0] - 1] + ysum_list[P[i][1] - 1] - n + 1
        sum_max = max(sum, sum_max)
    return sum_max

def countingSort(tab, k, mode): # 0 - x, 1 - y
    n = len(tab)
    temp = [0] * k
    for i in range(n):
        temp[tab[i][mode]] += 1
    for j in range(1, k):
        temp[j] += temp[j - 1]
    return temp

tab = [4,2,5,1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
