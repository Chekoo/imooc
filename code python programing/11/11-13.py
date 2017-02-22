#coding=utf-8
# def mult(x, y):
#     return x * y
#
# print reduce(mult, range(1, 5))
#
# print reduce(lambda x, y:x*y, range(1, 5))


import time

def fun1(n):
    '''迭代'''
    total = 1
    for each in range(1, n):
        total += total * each
    return total


def fun2(n):
    '''reduce'''
    return reduce(lambda x,y:x*y, range(1, n))

def fun3(n):
    '''递归'''
    if n == 1 or n == 0:
        return 1
    return n * fun3(n - 1)

def timeit(func, *nkwargs, **kwargs):
    start = time.clock()
    try:
        retval = func(*nkwargs, **kwargs)
        result = (time.clock() - start, retval)
    except:
        result = (time.clock()-start, False)
    return result

def test(n):
    funcs = (fun1, fun2, fun3)

    for eachFunc in funcs:
        retval = timeit(eachFunc, n)
        if retval[1] != False:
            print '%s time is %s' % (eachFunc.__name__, retval[0])
        else:
            print 'ERROR'

if __name__ == '__main__':
    test(5)