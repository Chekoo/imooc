#coding=utf-8
import time

def timeit(func, *nkwargs, **kwargs):
	start = time.clock()
	try:
		retval = func(*nkwargs, **kwargs)
		result = (time.clock()-start, retval)
	except:
		result = (time.clock()-start, False)
	return result

def test():
	funcs = (int, long, float)
	vals = （1234， 12.34，'1234', '12.34')
    
    for eachFunc in funcs:
    	print '_' * 20
    	for eachVal in vals:
    		retval = timeit(eachFunc, eachVal)
    		if retval[1] != False:
    			print '%s time is %s' % (eachFunc.__name__, retval[0])
    		else:
    			print 'Error'

if __name__ == '__main__':
	test()