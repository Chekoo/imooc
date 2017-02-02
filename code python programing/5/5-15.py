#coding=utf-8
def comdiv(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

def commul(a, b):
    return a * b / comdiv(a, b)

comdiv(4, 6)
commul(3, 6)