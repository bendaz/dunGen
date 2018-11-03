from random import *

def dx(x):
	result = randint(1,x)
	return result

def ydx(y,x):
	result = 0
	for roll in range(y):
		result = result + dx(x)
	return result

def gaussian(minimum, maximum):
	mu = ((minimum + maximum) / 2)
	sigma = (mu + ((maximum-mu) / 3))
	return random.gauss(mu,sigma)

def rollStatSet():
	sets = []
	for rollSet in range(1,3):
		tempSet = []
		while(1):
			while(1):
				tempRoll = []
				for dice in range(1,5):
					tempRoll.append(dx(6))
				tempRoll.remove(min(tempRoll))
				if (sum(tempRoll) >= 8):
					tempSet.append(sum(tempRoll))
					break
			if (len(tempSet) == 7):
				tempSet.remove(min(tempSet))
				sets.append(tempSet)
				break
	if (sum(sets[0]) > sum(sets[1])):
		return sets[0]
	else:
		return sets[1]
