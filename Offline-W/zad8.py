from zad8testy import runtests
from math import inf

# f(i, j) = minimalna suma odległości biurowców z pozycji X[0], . . . , X[i] do przydzielonych im
# działek, przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji Y [j].
# wynik: min(f(i, n)), n = 0...j
# f(0, n) = abs(X[0] - Y[n]), n = 0...m - n + 1
# f(i, j) = min(f(i - 1, s)) + abs(X[i] - Y[j]), s = i - 1 - (m - n + 1)...i - 1

def parking(X,Y):
  n = len(X)
  m = len(Y)
  minimum = inf
  F = [[inf for _ in range (m)] for _ in range (n)]
  for i in range (m - n + 1):
    F[0][i] = abs(X[0] - Y[i])
  #for a in range (1, n):
  #  F[a][a] = F[a - 1][a - 1] + abs(X[a] - Y[a])
  temp = [0 for _ in range (m - n + 1)]
  temp2 = [0 for _ in range (m - n + 1)]
  for i in range(m - n + 1):
    temp[i] = F[0][i]

  for x in range (1, n):
    i = 0
    lowest = inf
    for y in range (x, x + (m - n + 1)):
      lowest = min(lowest, temp[i])
      if y >= m: continue
      F[x][y] = abs(X[x] - Y[y]) + lowest
      #print('temp: ',(temp[0:i + 1]))
      temp2[i] = F[x][y]
      i += 1
    #print('temp2: ', temp2)
    for lol in range (m - n + 1):
      #print(temp[lol])
      temp[lol] = temp2[lol]
      #print(temp[lol])
    #print('temp1: ', temp)
  for i in range (n - 1, m):
    minimum = min(minimum, F[n - 1][i])
  #print(F, temp)
  return minimum



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
