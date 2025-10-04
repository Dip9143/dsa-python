class Array():
	""" A simple array class and basic operation for the array"""

	def __init__(self, initialize):
		self.__a = [None]*initialize
		self.__nItems = 0

	def insert(self, item):
		self.__a[self.__nItems] = item
		self.__nItems += 1

	def search(self, key):
		for j in range(self.__nItems):
			if self.__a[j] == key:
				return j
		return None

	def delete(self, item):
		index = self.search(item)
		if index is not None:
			self.__nItems -= 1
			for j in range(index, self.__nItems):
				self.__a[j] = self.__a[j + 1]
			self.__a[self.__nItems] = None
			return True
		return False

	def traverse(self):
		for j in range(self.__nItems):
			print(self.__a[j], end = " ")
		print("\n-------------")
