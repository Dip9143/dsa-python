def bubble(li):
	for outer in range(len(li) - 1, 0, -1):
		for inner in range(outer):
			if li[inner] > li[inner + 1]:
				li[inner], li[inner + 1] = li[inner + 1], li[inner]

li = list(range(10, 0, -1))
print("Original array: ", li)
bubble(li)
print("Sorted array: ", li)