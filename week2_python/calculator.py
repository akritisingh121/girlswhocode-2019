def add(x, y):
	return (x+y)

def subtract(x, y):
	return (x-y)

def average(numbers):
	return sum(numbers)/len(numbers)

def absolute_value(x):
	if x < 0:
		return x * -1
	else:
		return x

def factorial(x):
	factorial = 1
	for i in range(1, x+1):
		factorial = factorial * i
	return factorial
