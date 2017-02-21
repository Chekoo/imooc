from random import randint
def randGen(aList):
	while len(aList) > 0:
		yield aList.pop(randint(0, len(aList)))