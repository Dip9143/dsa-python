class OrderedArray():

	def __init__(self, initialize):
		self.__a = [None]*initialize
		self.__nItems = 0

	def __len__(self):
		return self.__nItems

	def __str__(self):
		ans = "["
		for j in range(self.__nItems):
			if len(ans) > 1:
				ans += ", "
			ans += str(self.__a[j])
		ans += "]"
		return ans

	def find(self, item):
		lo = 0
		hi = self.__nItems - 1

		while(lo <= hi):

			mid = (lo + hi) // 2
			if self.__a[mid] == item:
				return mid
			elif self.__a[mid] > item:
				hi = mid - 1
			else:
				lo = mid + 1

		return lo

	def search(self, key):
		index = self.find(key)

		if index < self.__nItems and self.__a[index] == key:
			print("Found")
		else:
			print("Not Found")

	def insert(self, item):
		if self.__nItems >= len(self.__a):
			raise Exception("Index Out of range")

		index = self.find(item)

		for j in range(self.__nItems, index, -1):
			self.__a[j] = self.__a[j - 1]
		self.__a[index] = item 
		self.__nItems += 1

	def delete(self, item):
		index = self.find(item)

		if index >= self.__nItems:
			print("Item is not in the array")
			return

		self.__nItems -= 1
		for j in range(index, self.__nItems):
			self.__a[j] = self.__a[j + 1]

		self.__a[self.__nItems] = None



		

