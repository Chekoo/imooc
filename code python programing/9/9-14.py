#coding=utf-8
'''计算器程序，模仿内建函数eval()'''
import sys
import os

def new_eval(num):
    if num[1] == '+':
        return int(num[0]) + int(num[2])
    elif num[1] == '-':
        return int(num[0]) - int(num[2])
    elif num[1] == '*':
        return int(num[0]) * int(num[2])
    elif num[1] == '/':
        return int(num[0]) / int(num[2])
    elif num[1] == '%':
        return int(num[0]) % int(num[2])
    elif num[1] == '**':
        return int(num[0]) ** int(num[2])
    else:
        return 'error operator'

if __name__ == '__main__':
    if sys.argv[1:][0] == 'print':
        with open('result.txt') as fobj:
            print fobj.read()
        os.remove('result.txt')
    else:
        with open('result.txt', 'a+') as fobj:
            fobj.write(''.join(sys.argv[1:]))
            fobj.write('\n')
            fobj.write(str(new_eval(sys.argv[1:])))
            fobj.write('\n')
        print 'The result is %d' % (new_eval(sys.argv[1:]))