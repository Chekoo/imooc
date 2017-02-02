from math import pi

def square(length):
    area =  length * 2
    print 'The area of square is %0.2f' % area

def cube(length):
    volume = length ** 3
    print 'The volume of cube is %0.2f' % volume

def circle(radius):
    area = pi * radius ** 2
    print 'The area of circle is %0.2f' % area

def sphere(radius):
    volume = 4 * pi * radius ** 2
    print 'The volume of sphere is %0.2f' % volume

if __name__ == "__main__":
    try:
        print 'Please input the number'
        num = float(raw_input())
        square(num)
        cube(num)
        circle(num)
        sphere(num)
    except ValueError, e:
        print 'Input Error'


