from SimpleStack import *

stack = SimpleStack(100)
exp = str(input("Enter an expression: "))
errors = 0

for pos, letter in enumerate(exp):

	if letter in "[{(":
		stack.push(letter)

	elif letter in ")}]":
		if stack.isEmpty():
			print("Error at position", pos)
			errors += 1
		else:
			poped = stack.pop()

			if not ((poped == "{" and letter =="}") or (poped == "(" and letter ==")") or (poped == "[" and letter =="]")):
				print("Error at position", pos)
				errors += 1

if stack.isEmpty() and errors == 0:
	print("Delimiters balance in expression", exp)

elif not stack.isEmpty():
	print("Expression missing right delimiters for", stack)
