#coding=utf-8
print 'Enter the experssion'
experssion = raw_input('> ')

if len(experssion.split('+')) == 2:
    try:
        splitExpressoon = experssion.split('+')
        a = float(splitExpressoon[0])
        b = float(splitExpressoon[1])
        print a + b
    except ValueError, e:
        print 'input ValueError'
elif len(experssion.split('-')) == 2:
    try:
        splitExpressoon = experssion.split('-')
        a = float(splitExpressoon[0])
        b = float(splitExpressoon[1])
        print a - b
    except ValueError, e:
        print 'input ValueError'
elif len(experssion.split('*')) == 2:
    try:
        splitExpressoon = experssion.split('*')
        a = float(splitExpressoon[0])
        b = float(splitExpressoon[1])
        print a * b
    except ValueError, e:
        print 'input ValueError'
elif len(experssion.split('%')) == 2:
    try:
        splitExpressoon = experssion.split('%')
        a = float(splitExpressoon[0])
        b = float(splitExpressoon[1])
        print a % b
    except ValueError, e:
        print 'input ValueError'
elif len(experssion.split('/')) == 2:
    try:
        splitExpressoon = experssion.split('/')
        a = float(splitExpressoon[0])
        b = float(splitExpressoon[1])
        print a / b
    except ValueError, e:
        print 'input ValueError'
elif len(experssion.split('**')) == 2:
    try:
        splitExpressoon = experssion.split('**')
        a = float(splitExpressoon[0])
        b = float(splitExpressoon[1])
        print a ** b
    except ValueError, e:
        print 'input ValueError'
else:
    print '你不会用！'

#快速方法
def calc(newstr):
    num = newstr.split(" ")
    if num[1] == '+':
        return float(num[0]) + float(num[2])
    elif num[1] == '-':
        return float(num[0]) - float(num[2])
    elif num[1] == '*':
        return float(num[0]) * float(num[2])
    elif num[1] == '/':
        return float(num[0]) / float(num[2])
    elif num[1] == '**':
        return float(num[0]) ** float(num[2])
    elif num[1] == '%':
        return float(num[0]) % float(num[2])
    else:
        return 'error'

number = raw_input()
calc(number)
