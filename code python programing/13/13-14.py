#coding=utf-8
import os
def cmdDir():
    dirName = os.getcwd()
    for i in os.listdir(dirName):
        print dirName + '\\' + i
def cmdmore(cmd):
    fileName = cmd.split(' ')[1]
    with open(fileName) as fobj:
        for line in fobj:
            print line
def cmdtype(cmd):
    fileName = cmd.split(' ')[1]
    type(fileName)
def cmdcopy(cmd):
    oldFile = cmd.split(' ')[1]
    newFile = cmd.split(' ')[2]
    with open(oldFile, 'r') as foldObj:
        with open(newFile, 'w') as fnewObj:
            for line in foldObj:
                fnewObj.write(line)
def cmdren(cmd):
    cmdcopy(cmd)
    delFile = cmd.split(' ')[1]
    os.remove(delFile)
def cmddel(cmd):
    delFile = cmd.split(' ')[1]
    os.remove(delFile)
def DOS():
    while True:   #find()方法检测字符串是否包含子字符串str，如果指定beg(开始)和end(结束)范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
        cmd = raw_input('please enter: ls, more, cat, cp, mv or rm')
        if cmd.find('ls') != -1:
            cmdDir()
        elif cmd.find('more') != -1:
            cmdmore(cmd)
        elif cmd.find('cat') != -1:
            cmdtype(cmd)
        elif cmd.find('cp') != -1:
            cmdcopy(cmd)
        elif cmd.find('mv') != -1:
            cmdren(cmd)
        elif cmd.find('rm') != -1:
            cmddel(cmd)
        else:
            print 'sorry, command is wrong.please enter:ls, more, cat, cp, mv or rm'

if __name__ == "__main__":
    print DOS()