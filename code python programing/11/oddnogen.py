#coding=utf-8
from random import randint
#1
def odd(n):
	return n % 2

allNums = []
for eachNum in range(9):
	allNums.append(randint(1, 99))
print filter(odd, allNums)



#2   list综合使用成为filter()替代者
allNums = []
for eachNum in range(9):
	allNums.append(randint(1, 99))
print filter(lambda n )


#3   通过列表解析
from random import randint as ri
print [n for n in [ri (1, 99) for i in range(9)] if n % 2]