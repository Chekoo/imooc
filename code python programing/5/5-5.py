#coding=utf-8
#简单的方法，通过循环解决
def change(money):
    list = [24, 10, 5, 1]
    count = 0
    for i in list:
        result = divmod(money, i)
        count += result[0]
        money = result[1]
        print '%d %dcoins' %(count, i)

money = float(raw_input('input the money that less than 1 dooler: '))
change(money)

#粗糙方法
try:
    money = float(raw_input('input the money that less than 1 doller: '))
    if money > 1:
        print 'money is too large'
    elif 0 < money < 1:
        temp = int(money * 100)
        (N25, temp) = divmod(temp, 25)
        print '%d 25 coins.' % N25
        (N10, temp) = divmod(temp, 10)
        print '%d 10 coins.' % N10
        (N5, temp) = divmod(temp, 5)
        print '%d 5 coins.' % N5
        (N1, temp) = divmod(temp, 1)
        print '%d 1 coins.' % N1
    else:
        print 'Please input larger than 0'

except ValueError, e:
    print 'You must ipnut a digits.'