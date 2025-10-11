def selection(li):
	for outer in range(len(li) - 1):
		min = outer
		for inner in range(outer + 1, len(li)):
			if li[min] > li[inner]:
				min = inner
		if min != outer:
			li[min], li[outer] = li[outer], li[min]

li = list(range(100, 0, -1))
print("Original array: ", li)
selection(li)
print("Sorted array: ", li)