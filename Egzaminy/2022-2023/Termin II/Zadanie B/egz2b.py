from egz2btesty import runtests
from math import inf

# założenia:
# f(i, j) - minimalna suma odległości biurowców z pozycji X[0], . . . , X[i] do przydzielonych im
# działek, przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji Y [j].
# wstępne warunki:
# f(0, j) = abs(X[0] - Y[j]), j = 0...m-1

# dorobić opis :))


def parking(X,Y):
	n = len(X)
	m = len(Y)
	dynamic_distances = [[inf for _ in range (m)] for _ in range (n)]
	minimum = inf
	for slot in range (m - n + 1):
		dynamic_distances[0][slot] = abs(X[0] - Y[slot])
		minimum = min(minimum, dynamic_distances[0][slot])
	#print(dynamic_distances)
	for building in range (1, n):
		minimum = dynamic_distances[building - 1][building - 1]
		for parking_slot in range (building, building + m - n + 1):
			dynamic_distances[building][parking_slot] = minimum + abs(X[building] - Y[parking_slot])
			minimum = min(minimum, dynamic_distances[building - 1][parking_slot])
	return min(dynamic_distances[n - 1])




  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )

X = [3,6,10,14]
Y = [1,4,5,10,11,13,17]

print(parking(X, Y))