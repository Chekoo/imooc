#coding=utf-8
import time
class Date(object):
    def __init__(self, time = time.ctime()):
        self.time = time
    def choice(self, choiceTime):
        date = []
        date = self.time.split(' ')
        dateDict = {}
        dateDict['MMY'] = date[1] + '/' + date[2] + '/' + date[4][2:]
        dateDict['MDYY'] = date[1] + '/' + date[2] + '/' + date[4]
        dateDict['DMY'] = date[2] + '/' + date[1] + '/' + date[4][2:]
        dateDict['DMYY'] = date[2] + '/' + date[1] + '/' + date[4]
        dateDict['MODDY'] = date[1] + ' ' + date[2] + ',' + date[4]
        return dateDict[choiceTime]

if __name__ == '__main__':
    date1 = Date()
    while True:
        print "'MMY' --> MM/DD/YY"
        print "'MDYY' ==> MM/DD/YYYY"
        print "'DMY' ==> DD/MM/YY"
        print "'DMYY' ==> DD/MM/YYYY"
        print "'MODDY' ==> Mon DD, YYYY"
        choiceTime = raw_input('please enter your choice(q to quit): ')
        if choiceTime == 'q':
            break
        print date1.choice(choiceTime)