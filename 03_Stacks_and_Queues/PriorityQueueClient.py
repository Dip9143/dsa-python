import PriorityQueue as PQ 


def identity(x):
	return x[0]

q = PQ.PriorityQueue(10)
for j in [(0, "Dip"), (0, "Nil"), (1, "Suvo"), (2, "Sudipto")]:
	q.insert(j)

print(q)
print(q.remove())
print(q)
