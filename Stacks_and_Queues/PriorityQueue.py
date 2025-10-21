def identity(x):
	return x

class PriorityQueue():

	def __init__(self, max, prioFunc=identity):
		self.__q = [None]*max
		self.__max = max 
		self.__prioFunc = prioFunc
		self.__nItems = 0

	def isEmpty(self):
		return self.__nItems == 0

	def isFull(self):
		return self.__nItems >= self.__max

	def insert(self, item):
		if self.isFull():
			raise IndexError("Queue Overload!!!")

		j = self.__nItems - 1

		while (j >= 0 and self.__prioFunc(item) >= self.__prioFunc(self.__q[j])):
			self.__q[j + 1] = self.__q[j]
			j -= 1
		self.__q[j + 1] = item
		self.__nItems += 1
		return True

	def remove(self):
		if self.isEmpty():
			raise IndexError("Queue Underflow!!!")

		self.__nItems -= 1
		front = self.__q[self.__nItems]
		self.__q[self.__nItems] = None

		return front

	def __str__(self):
		ans = "["
		j = 0
		while (j < self.__nItems):
			if len(ans) > 1:
				ans += ", "
			ans += str(self.__q[j])
			j += 1
		ans += "]"
		return ans 