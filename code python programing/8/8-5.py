#coding=utf-8
def getfactors(num):
    count = num / 2
    list1 = [x for x in range(2, count+1) if num % x == 0]
    if num == 1:
        list1.append(1)
    else:
        list1.extend([1, num])
    list1.sort()
    return list1

if __name__ == '__main__':
    while True:
        for each in xrange(1, 15):
            print each, getfactors(each)
        break