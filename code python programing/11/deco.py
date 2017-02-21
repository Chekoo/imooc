#coding=utf-8
from time import ctime, sleep

def tsfunc(func):    #显示何时调用函数的时戳的装饰器
	def wrappedFunc():
		print ('[%s] %s() called' % (ctime(), func.__name__))
		return func()
	return wrappedFunc

@tsfunc
def foo():   #定义使用foo()函数并用tsfunc()来装饰
	pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()