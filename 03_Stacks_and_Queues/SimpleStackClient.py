import SimpleStack as S 

stack = S.SimpleStack(10)

for j in range(10):
	stack.push(j)

print(stack)

for j in range(10):
	print(stack.pop())