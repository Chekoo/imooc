from types import IntType
import types
def displayNumType(num):
    print num, 'is',
    # if isinstance(num, int):
    #     print 'an integer'
    # elif isinstance(num, long):
    #     print 'a long'
    # elif isinstance(num, float):
    #     print 'a float'
    # elif isinstance(num, complex):
    #     print 'a complex number'
    # else:
    #     print 'not a number at all'
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(99999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')