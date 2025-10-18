import CirculerQueue as CQ  

queue = CQ.Queue(5)

for j in range(5):
	queue.insert(j)
print(queue)
print("Peek:", queue.peek())

for j in range(5):
	print(queue.remove())