#coding=utf-8
filename1 = raw_input('Enter a filename1: ')
filename2 = raw_input('Enter a filename2: ')

with open(filename1) as fobj1:
    with open(filename2, 'w') as fobj2:
        for i in fobj1:
            fobj2.write(i)
    with open(filename2) as fobj2:
        print fobj2.read()
fobj1.close()
fobj2.close()