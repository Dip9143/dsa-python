class Link():
	def __init__(self, datum, next=None):
		self.__data = datum
		self.__next = next

	def getData(self):
		return self.__data

	def setData(self, datum_new):
		self.__data = datum_new
		return True

	def getNext(self):
		return self.__next

	def setNext(self, new_next):
		if new_next is None or isinstance(new_next, Link):
			self.__next = new_next
			return True
		else:
			raise Exception("Next Link must be None or instance of Link class")

	def isLast(self):
		return self.__next is None

	def __str__(self):
		return str(self.__data)



