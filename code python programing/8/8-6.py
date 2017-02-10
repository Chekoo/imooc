#coding=utf-8
def isprime(num):
    if num == 1:
        return False
    count = num / 2
    while count > 1:
        if num % count == 0:
            return False
            break
        count -= 1
    else:
        return True

def getfactors(num):
    count = num / 2
    list1 = []
    while count > 1:
        if isprime(count) and num % count == 0:
            list1.append(count)
            num = num / count
            count = num /2
        else:
            count -= 1
    if num == 1:
        list1.append(1)
    else:
        list1.append(num)
    list1.sort()
    return list1

if __name__ == '__main__':
    for each in xrange(1, 26):
        print each, getfactors(each)