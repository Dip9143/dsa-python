from Link import *

def identity(x):
	return x

class LinkedList():
	def __init__(self):
		self.__first = None

	def getFirst(self):
		return self.__first

	def setFirst(self, link):
		if link is None or isinstance(link, Link):
			self.__first = link
		else:
			raise Exception("First link must be Link or None")

	def getNext(self):
		return self.getFirst()

	def isEmpty(self):
		return self.__first is None

	def first(self):
		if self.isEmpty():
			raise Exception("List is Empty!!!")

		return self.__first.getData()

	def traverse(self, func=print):
		link = self.getFirst()
		while link is not None:
			func(link.getData(), end=" --> ")
			link = link.getNext()
		print("None")

	def __len__(self):
		l = 0
		link = self.getFirst()
		while link is not None:
			l += 1
			link = link.getNext()

		return l

	def insert(self, datum):
		link = Link(datum, self.getFirst())
		self.setFirst(link)

	def find(self, goal, key=identity):
		link = self.getFirst()
		while link is not None:
			if key(link.getData()) == goal:
				return link 

			link = link.getNext()

	def search(self, goal, key=identity):
		link = self.find(goal, key=key)
		if link is not None:
			return link.getData()

	def insertAfter(self, goal, newDatum, key=identity):
		link = self.find(goal)
		if link is None:
			return False
		newLink = Link(newDatum, link.getNext())
		link.setNext(newLink)
		return True

	def deleteFirst(self):
		if self.isEmpty():
			raise Exception("The list is Empty")

		first = self.getFirst()
		self.setFirst(first.getNext())
		return first.getData()

	def delete(self, goal, key=identity):
		if self.isEmpty():
			raise Exception("The list is Empty")

		prev = self
		while prev.getNext() is not None:
			link = prev.getNext()
			if goal == key(link.getData()):
				prev.setNext(link.getNext())
				return link.getData()
			prev = link 



