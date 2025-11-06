class Array():

	def __init__(self, initialize):
		self.__a = [None]*initialize
		self.__nItems = 0

	def __len__(self):
		return self.__nItems

	def get(self, n):
		if n >= 0 and n < self.__nItems:
			return self.__a[n]

	def set(self, n, item):
		if n >= 0 and n < self.__nItems:
			self.__a[n] = item

	def insert(self, item):
		if self.__nItems < len(self.__a):
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
		print("\n--------------------------------")
		for j in range(self.__nItems):
			print(self.__a[j], end = " ")
		print("\n--------------------------------")

