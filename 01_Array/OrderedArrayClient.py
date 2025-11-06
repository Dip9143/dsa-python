import OrderedArray as OA 

arr = OA.OrderedArray(5)
arr.insert(1)
arr.insert(2)
arr.insert(3)
arr.insert(4)
arr.insert(5)
print(str(arr))
arr.search(5)
arr.search(0)
arr.delete(1)
arr.delete(2)
arr.delete(3)
arr.delete(4)
arr.delete(5)
arr.delete(1)
print(str(arr))


