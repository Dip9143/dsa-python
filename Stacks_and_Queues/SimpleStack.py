class SimpleStack():

	def __init__(self, max):
		self.__s = [None]*max
		self.__top = -1

	def isEmpty(self):
		return self.__top == -1

	def isFull(self):
		return self.__top == len(self.__s) - 1

	def push(self, item):
		if self.isFull():
			raise IndexError('Stack overflow on expression')

		self.__top += 1
		self.__s[self.__top] = item

	def pop(self):
		if self.isEmpty():
		    raise IndexError("Stack underflow")


		top_element = self.__s[self.__top]
		self.__s[self.__top] = None
		self.__top -= 1
		return top_element

	def peek(self):
	    if self.isEmpty():
	        raise IndexError("Stack is empty")
	    return self.__s[self.__top]

	def __str__(self):
		ans = "["
		for j in range(self.__top, -1, -1):
			if len(ans) > 1:
				ans += ", "
			ans += str(self.__s[j])
		ans += "]"
		return ans

