#coding=utf-8
import re
import string

#1
def test1():
    bt = 'bat|bit|but|hat|hit|hut'
    inputstr = raw_input('input neeeds to match String: ')
    m = re.match(bt, inputstr)
    if m is not None:
        print (m.group())
    else:
        print 'not match'

#2
def test2():
    bt = '(.*)\s(.*)'
    inputstr = raw_input('请输入您的姓名，姓与名之间用空格隔开\n')
    m = re.methch(bt, inputstr)
    if m is not None:
        print('您的姓是：%s')

def test3():
    bt = '(.*),(.*|.*\s.*)'
    inputstr = raw_input('输入你的姓名，姓与名之间用逗号隔开: ')
    m = re.match(bt, inputstr)
    if m is not None:
        print '你的姓是: %s' % m.group(1)
        print '你的名是: %s' % string.replace(m.group(2), ' ', '')
        print '你的姓名是: %s' % string.replace(m.group(0), ' ', '')
    else:
        print '匹配失败'

def test4():
    bt = '\w.*'
    inputstr = raw_input('enter string: ')
    m = re.match(bt, inputstr)
    if m is not None:
        print '%s is a string' % m.group()
    else:
        print '%s is not a string' % inputstr

def test5():
    stress = '(\d+\s)+(\S+\s?)+'
    inputstr = raw_input('Enter street string:\n ')
    m = re.match(stress, inputstr)
    if m is not None:
        print '%s is a street' % m.group()
    else:
        print '%s is not a street' % inputstr

def test6():
    bt = '(^www)\.(\S+)\.([com|edu|cn|net])'
    inputstr = raw_input('Enter URL: ')
    m = re.match(bt, inputstr)
    if m is not None:
        print '%s is a URL' % m.group()
    else:
        print '%s is not a URL' % inputstr

def test7_10():
    bt7 = '\d+'
    bt8 = '\d+[L]?'
    bt9 = '\d+.\d+'
    bt10 = '\d'
    inputstr7 = raw_input('enter int number: ')
    inputstr8 = raw_input('enter long int number: ')
    inputstr9 = raw_input('enter float number: ')
    inputstr10 = raw_input('enter complex number: ')
    m7 = re.match(bt7, inputstr7)
    m8 = re.match(bt8, inputstr8)
    m9 = re.match(bt9, inputstr9)
    m10 = re.match(bt10, inputstr10)
    if m7 is not None:
        print 'int: %s' % m7.group()
    if m8 is not None:
        print 'long int: %s' % m8.group()
    if m9 is not None:
        print 'float: %s' % m9.group()
    if m10 is not None:
        print 'complex: %s' % m10.group()

def test11():
    bt = "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}]~-]+)*@(?:[\w](?:[\w-]*[\w]?\.)+[\w](?:[\w-]*[\w])?"
    inputstr = raw_input('Enter E-mail: ')
    m = re.match(bt, inputstr)
    if m is not None:
        print 'E-mail is: %s' % m.group()
    else:
        print 'not a email'

def test12():
    bt = '[a-zA-z]+://[^\s]*'
    inputstr = raw_input('Enter URL: ')
    m = re.match(bt, inputstr)
    if m is not None:
        print 'URL is %s' % m.group()
    else:
        print 'not a URL'

def test13():
    data = "<type 'int'>"
    patt = "<type\s'(\w+)'>"
    m = re.search(patt, data)
    if m is not None:
        print m.group()

def test14():
    date = '1[0-2]'
    m = re.match(date, '12')
    print m.group()

def test15():
    patt = '([0-9]{4}-?[0-9]{6}-?[0-9]{5})|([0-9]{4}-?[0-9]{4}-?[0-9]{4}-[0-9]{4})'
    inputstr = raw_input('Enter yoru card number: ')
    m = re.match(patt, inputstr)
    if m is not None:
        print 'right: %s' % m.group()
    else:
        print 'not a card number'

def test17_25():
    patt17 = 'Thu'
    patt19 = '\s(\d{1,2}):(\d{1,2}):(\d{1,2})\s'
    patt20 = "[\w!#$%'*+/=?^_`{|}~-]+(?:\.[\w!#$%'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w]?\.)+[\w](?:[\w-]*[\w])?"
    patt21 = "\s\w+\s"
    patt22 = '\s[0-9]{4}'
    patt24 = '(\w+)@(\w+)\.(\w+)'
    patt25 = '(\w+)@(\w+)\.(\w+)'
    f = open('redata.txt', 'r')
    count = 0
    for eachLine in f:
        m = re.findall(patt17, eachLine)
        count += len(m)

        strTemp = str(eachLine)

        m19 = re.search(patt19, strTemp)
        print '19_____', m19.group()

        m20 = re.search(patt20, strTemp)
        print '20_____', m20.group()

        m21 = re.search(patt21, strTemp)
        print '21_____', m21.group()

        m22 = re.search(patt22, strTemp)
        print '22_____', m22.group()

        m24 = re.search(patt24, strTemp)
        m24temp = re.split('@', m24.group())
        m24real = m24temp[0]+m24temp[1]
        print '24_____', m24real
    print 'the count of: %s is %d' % (patt17, count)
    f.close()

def test26():
    patt = '\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*'
    f = open('redata.txt', 'r')
    for eachLine in f:
        m = re.search(patt, str(eachLine))
        print m.group()
        m26 = re.sub(patt, 'hello@163.com', str(eachLine))
        print m26

def test27():
    patt = '(\S+)\s(\d+)\s\d+:\d+:\d+\s(\d+)'
    f = open('redata.txt', 'r')
    for eachLine in f:
        m = re.search(patt, str(eachLine))
        try:
            print '%s-%s-%s' % (m.group(1), m.group(2), m.group(3))
        except(AttributeError), djag:
            pass

def test28():
    patt = '(\d{3}-)?\d{3}-\d{4}'
    m = re.match(patt, '800-555-1212')
    print m.group()
    m2 = re.match(patt, '555-1212')
    print m2.group()

def test29():
    patt = '\(?\d{3}\)?-?\d{3}-\d{4}'
    m = re.match(patt, '800-555-1212')
    print m.group()
    m2 = re.match(patt, '555-1212')
    if m2 is not None:
        print m2.group()
    else:
        print 'm2 not match'

    m3 = re.match(patt, '(800)555-1212')
    print m3.group()



if __name__ == "__main__":
    test29()

















