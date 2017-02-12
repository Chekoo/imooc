#coding=utf-8
# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形

def change(str):
    return str.title()

str = raw_input('enter a string')
print change(str)