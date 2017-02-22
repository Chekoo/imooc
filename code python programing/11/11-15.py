#coding=utf-8
#向后打印
def printLeft(str):
    if str:
        print str[0]
        return printLeft(str[1:])

def printRight(str):
    if str:
        print str[-1]
        return printRight(str[:-1])

if __name__ == '__main__':
    str = raw_input('Enter a string: ')
    print printLeft(str)
    print printRight(str)