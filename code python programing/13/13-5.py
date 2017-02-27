#coding=utf-8
#创建一个有序数值对(x, y)组成的Point类，它代表某个点的X坐标和Y坐标，X坐标和Y坐标在实例化时被传递给构造器，如果没有给出他们的值，则默认为坐标的原点
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def get_xy(self):
        return (self.__x, self.__y)
    def set_xy(self, point):
        self.__x, self.__y = point
    def __str__(self):
        return '%d:%d' % (self.__x, self.__y)

    __repr__ = __str__
    point = property(get_xy, set_xy)

if __name__ == "__main__":
    p = Point(1,2)
    print p
    p.point = 4, 5
    print p
    p.point = 7, 8
    print p
