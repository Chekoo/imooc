def grade(num):
    if 90 <= num <= 100:
        print 'A'
    elif 80 <= num <= 89:
        print 'B'
    elif 79 <= num <= 79:
        print 'C'
    elif 60 <= num <= 69:
        print 'D'
    elif 0 <= num <= 59:
        print 'F'
    else:
        print 'The num is invalid.'

try:
    num = int(raw_input('input a num: '))
    grade(num)
except ValueError, e:
    print 'You must input digits.'