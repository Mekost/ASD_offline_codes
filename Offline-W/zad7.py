from zad7testy import runtests

from math import inf

def maze(L):
    n = len(L)
    F = [[-inf for _ in range (n)] for _ in range (n)]
    going_down = [[-inf for _ in range (n)] for _ in range (n)]
    going_up = [[- inf for _ in range (n)] for _ in range (n)]
    F[0][0] = going_down[0][0] = going_up[0][0] = 0
    for column in range (n):
        for row_down in range (1, n):
            if L[row_down][column] == '#':
                going_down[row_down][column] = -inf
            elif going_down[row_down - 1][column] != -inf:
                going_down[row_down][column] = max(going_down[row_down - 1][column] + 1, going_down[row_down][column])
        for row_up in range (n - 2, -1, -1):
            if L[row_up][column] == '#':
                going_up[row_up][column] = -inf
            elif going_up[row_up + 1][column] != -inf:
                going_up[row_up][column] = max(going_up[row_up + 1][column] + 1, going_up[row_up][column])
        for next in range (n):
            F[next][column] = max(going_down[next][column], going_up[next][column])
            if column != n - 1:
                if F[next][column] != -inf:
                    if L[next][column + 1] != '#':
                        going_up[next][column + 1] = F[next][column] + 1
                        going_down[next][column + 1] = F[next][column] + 1
    #print(going_down)
    #print(going_up)
    return F[n - 1][n - 1] if F[n - 1][n - 1] != -inf else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
