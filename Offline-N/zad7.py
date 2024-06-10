from zad7testy import runtests
#zlozonosc n^2. dla kazdej kolumny idziemy osobno w górę i w dol, ustalajac przy tym
#
def maze(L):
    n=len(L)
    dist=[[-1 for i in range(n)]for j in range(n)]
    dist[0][0]=0
    def right(a):#wartości z kolumny a dajemy na kolumnę a+1, o ile to możliwe
       for row in range(n):
           if L[row][a+1]!="#" and dist[row][a]!=-1:
               dist[row][a+1]=dist[row][a]+1
           else:
               dist[row][a + 1]=-1

    def up(a):
        t=[dist[row][a] for row in range(n)]

        for row in range(n-2,-1,-1):#idąc w góre aktualizujemy wartosci
            if t[row+1]!=-1 and L[row][a]!="#":
                t[row]=max(t[row],t[row+1]+1)
        return t
    def down(a):
        t = [dist[row][a] for row in range(n)]

        for row in range(1,n):
            if t[row-1]!=-1 and L[row][a]!="#":
                t[row]=max(t[row],t[row-1]+1)
        return t

    def update(tup,tdown):#aktualizuje teraz tablice dist z najlepszymi wartosciami z obu sposobow chodzenia po komnatach
        tup = tup
        tdown = tdown
        for row in range(n):
            dist[row][col] = max(tup[row], tdown[row])

    for col in range(n):
        update(up(col),down(col))
        if col!=n-1:
            right(col)



    return dist[n-1][n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )