from random import *

N = random.randint(2, 100)
randlist = random.sample(xrange(0, 2**31 - 1), N)
randlist.sort()
print randlist

#第二种方法
N = randint(1, 101)
a = 2**31 - 1
list1 = []
for i in range(0, N):
    list1.append(randint(0, a))
print list1


list2 = []
N2 = randint(1, N)
count = N - 1
for i in range(0, N2):
    s = list1.pop(randint(0, count))
    count -= 1
    list2.append(s)
list2.sort()
print list2

