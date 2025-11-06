class Queue():

	def __init__(self, max):
		self.__max = max 
		self.__q = [None]*max 
		self.__front = 1
		self.__rear = 0
		self.__nItems = 0

	def isEmpty(self):
		return self.__nItems == 0

	def isFull(self):
		return self.__nItems == self.__max

	def insert(self, item):
		if self.isFull():
			raise IndexError("Queue Overflow!!!")

		self.__rear += 1
		if (self.__rear == self.__max):
			self.__rear = 0

		self.__q[self.__rear] = item
		self.__nItems += 1
		return True 

	def remove(self):
		if self.isEmpty():
			raise IndexError("Queue underflow!!!")

		front_element = self.__q[self.__front]
		self.__q[self.__front] = None
		self.__front += 1
		if (self.__front == self.__max):
			self.__front = 0
		self.__nItems -= 1

		return front_element

	def peek(self):
		if self.isEmpty():
			raise IndexError("Queue underflow!!!")

		return self.__q[self.__front]

	def __str__(self):
		ans = "["
		i = self.__front
		for j in range(self.__nItems):
			if len(ans) > 1:
				ans += ", "
			ans += str(self.__q[i])
			i = (i + 1)%self.__max
		ans += "]"
		return ans
