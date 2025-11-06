from LinkedList import *

def identity(x):
	return x


newList = LinkedList()
newList.insert("Orange")
newList.insert("Apple")
newList.insert("Guava")
newList.traverse()
newList.deleteFirst()
newList.traverse()
newList.delete("Orange")
newList.traverse()