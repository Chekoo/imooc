#coding=utf-8
import os
import sys
num = []
'''将所有路径文件名全部提出来'''
def fun(dirName):
    for i in os.listdir(dirName):
        if os.path.isdir(dirName + '\\' + i):
            fun(dirName + '\\' + i)
        else:
            num.append(dirName + '\\' + i)
fun(r'C\:python\lib')
hasDoc = False
strTemp = ''
fileobj1 = open('hasdoc.txt', 'a+')
fileobj2 = open('nodoc.txt', 'a+')
for i in num:
    fobj = open(i)
    for each in fobj:
        if (not hasDoc) and each.startswith('"""'):
            hasDoc = True
        elif hasDoc and each.startswith('"""'):
            hasDoc = False
            strTemp += each
            break
        if hasDoc:
            strTemp += each
        else:
            break
    if strTemp != '':
        fileobj1.write('文件名: ' + i + '\n')
        fileobj1.write('__doc__ is: ' + '\n')
        fileobj1.write(strTemp + '\n')
    else:
        fileobj2.write('文件名: ' + i + '\n')
    strTemp = ''
    fobj.close()
fileobj1.close()
fileobj2.close()