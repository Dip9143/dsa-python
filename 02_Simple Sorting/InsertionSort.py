def insertion(li):
	for outer in range(1, len(li)):
		temp = li[outer]
		inner = outer

		while (inner > 0 and temp < li[inner - 1]):
			li[inner] = li[inner - 1]
			inner -= 1

		li[inner] = temp

li = list(range(10, 0, -1))
print("Original array: ", li)
insertion(li)
print("Sorted array: ", li)