import BadArray as BA 

my_arr = BA.Array(5)
for j in range(5):
	my_arr.insert(j*100)

my_arr.traverse()
print(my_arr.delete(400))
print(my_arr.delete(300))
print(my_arr.delete(200))
print(my_arr.delete(100))
print(my_arr.delete(0))
my_arr.traverse()