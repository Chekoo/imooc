import os
import random
def fun(ch, countNum, length):
    firstLength = length
    num = []
    while firstLength - countNum:
        chara = random.choice(xrange(255))
        if ch == chara:
            continue
        else:
            num.append(chara)
            firstLength -= 1
    for i in range(countNum):
        num.append(ch)
    new_num = []
    while length:
        i = int(random.random() * length)
        new_num.append(num[i])
        del num[i]
        length -= 1
    return new_num

if __name__ == '__main__':
    num = fun(25, 10, 15)
    for item in num:
        print '{0:b}'.format(item)