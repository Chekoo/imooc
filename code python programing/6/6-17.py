#coding=utf-8
def myPop(list):
    list = list[1:-1]
    list_del = list[-1]
    print list
    print list_del

list = raw_input('please enter a list: ')
myPop(list)