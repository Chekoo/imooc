#coding=utf-8
def average(aList):
	return reduce((lambda x, y: x+y), aList)/float(len(aList))