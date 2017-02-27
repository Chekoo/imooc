#coding=utf-8
#多类型

class NumStr(object):
    def __init__(self, num = 0, string = ""):
        self.__num = num
        self.__string = string

    def __str__(self):  # define for str()   把顺序对的字符串表示形式为[num::str],实例用str()还是包含在printf语句中，都可以用__str__()来提供这种凡是
        return '[%d :: %r]' % self.__num, self.__string #第二个元素是字符串，使用__repr__()对代码进行转换，把%s替换成%r,这样用户可以看到由引号标记的字符串

    __repr__ = __str__   #__repr__()复制__str__()函数的引用，当实现__str__()后，一旦使用使用对象作为参数应用内建str()，解释器就会调用代码，对__repr__()也一样

    def __add__(self, other):  #define for s + o  Python用于定制类的特征之一是,我们可以重载操作符
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num, self.__string + other.__string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __mul__(self, num):  #define for o*n
        if isinstance(num, int):  #通过self.__class__()来实例化形成一个新的对象
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError, 'Illeagal argument type for built-in operation'

    def __nonzero__(self):    #False if both are     Python对象任何时候都有一个布朗值，对标准类型来说，类似0的数值或是一个空序列，或者是映射
        return self.__num or len(self.__string)   # 这个类，我们选择的数值必须为0，字符串为空作为一个实例有一个False值的条件

    def __norm_cval(self, cmpres):  # normalize cmp()  帮助我们重载__cmp__()的助手函数，目的是：把cmp()返回的正值转成1,负数为-1。
        return cmp(cmpres, 0)

    def __cmp__(self, other):   #define for cmp()
        return self.__norm_cval(
            cmp(self.__num, other.__num)) + self.__norm_cval(cmp(self.__string, other.__string))

if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string='boo')
    f = NumStr(1)
    s