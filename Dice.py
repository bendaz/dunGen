from random import *

def dx(x):
	result = randint(1,x)
	print(result)
	return result

def ydx(y,x):
	result = 0
	for roll in range(y):
		result = result + dx(x)
	print(result)
	return result