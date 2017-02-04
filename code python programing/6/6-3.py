#coding=utf-8
def order(num):
    a = []
    num = num.split()
    for n in reversed(sorted([int(i) for i in num])):    #重点加int()
        a.append(n)
    return a

if __name__ == '__main__':
    num = raw_input('Enter the number: ')
    print order(num)