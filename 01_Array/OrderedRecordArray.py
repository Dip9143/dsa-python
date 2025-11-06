def identity(x):
	return x

class OrderedRecordArray():
	def __init__(self, initialize, key_func=identity):
		self.__a = [None]*initialize
		self.__nItems = 0
		self.__key_func = key_func

	def __len__(self):
		return self.__nItems

	def traverse(self):
		print("Items: ", end = "")
		for j in range(self.__nItems):
			print(self.__a[j], end = " ")
		print()

	def find(self, key):
		low = 0
		high = self.__nItems - 1

		while (low <= high):
			mid = (low + high) // 2

			if self.__key_func(self.__a[mid]) == key:
				return mid

			elif self.__key_func(self.__a[mid]) < key:
				low = mid + 1

			else:
				high = mid - 1

		return low

	def insert(self, item):
		if self.__nItems >= len(self.__a):
			raise Exception("Array Overflow")

		index = self.find(self.__key_func(item))

		for j in range(self.__nItems, index, -1):
			self.__a[j] = self.__a[j - 1]
		self.__a[index] = item 
		self.__nItems += 1

	def search(self, item):
		index = self.find(self.__key_func(item))

		while(index < self.__nItems and self.__key_func(self.__a[index]) == self.__key_func(item) and self.__a[index] == item):
			print("Found")
			index += 1
	def delete(self, item):
		index = self.find(self.__key_func(item))

		if self.__a[index] is not None:
			self.__nItems -= 1
			for j in range(index, self.__nItems):
				self.__a[j] = self.__a[j + 1]
			self.__a[self.__nItems] = None
			print("One matched item deleted")
			return True
		else:
			print("Item not found")
			return False



