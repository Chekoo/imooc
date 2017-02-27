#coding=utf-8
class AddrBookEntry(object):
    def printFoo(self):
        print 'You invoked printFoo()!'

    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for: ', self.name

    def updatePhone(self, newph):
        self.phone = newph
        print 'Updated phone# for:', self.name


#创建子类
class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'  #员工地址簿类

    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.name

#创建一个类，跟踪引用计数
class InstCt(object):
    count = 0    #count是一个类属性

    def __init__(self):   #增加count
        InstCt.count += 1

    def __del__(self): #减少count
        InstCt.count -= 1

    def howMany(self):  #返回count
        return InstCt.count



#旅馆租房费用
class HotelRoomCalc(object):
    'Hotel room rate calculator'

    def __init__(self, rt, sales = 0.085, rm = 0.1):
        '''HotelRoomCalc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days = 1):
        'Calculate total; default to daily rate'
        daily = round((self.roomRate(1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

class NewAddrBookEntry(object):
    'new address book entry class'
    def __init__(self, nm, ph):
        self.name = Name(nm)
        self.phone = Phone(ph)
        print 'Created instance for:', self.name


#创建子类
class SubClassName(ParentClass1[, ParentClass2, ...]):
    'optional class documentation string'
    class_suite


class Parent(object):
    def parentMethod(self):
        print 'calling parent method'

class Child(Parent):
    def chileMethod(self):
        print 'calling child method'


class P:
    'P class'
    def __init__(self):
        print 'created an instance of', self.__class__.__name__

class C(P):
    pass


class P1(object):
    def foo(self):
        print 'called P1-foo()'

class P2(object):
    def foo(self):
        print 'called P2-foo()'

    def bar(self):
        print 'called P2-bar()'

class C1(P1, P2):
    pass

class C2(P1, P2):
    def bar(self):
        print 'called C2-bar()'

class GC(C1, C2):
    pass


class RouteFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), 'Value must be a float!'
        self.value = round(val, 2)



#包装类
class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        return getattr(self.__data, attr)




