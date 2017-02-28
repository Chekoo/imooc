#coding=utf-8

import sys
def foo():
    print 'show message'

sys.exitfunc = foo
print '123'