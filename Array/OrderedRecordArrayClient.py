import OrderedRecordArray as OR

def my_key_func(x):
	return x[1]

sample = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('e', 5)]

arr = OR.OrderedRecordArray(6, my_key_func)

for j in sample:
	arr.insert(j)

arr.traverse()
arr.search(('e', 5))
arr.delete(('e', 5))
arr.delete(('e', 5))
arr.delete(('e', 5))


arr.traverse()