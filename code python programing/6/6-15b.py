#coding=utf-8
from datetime import *
def birday_count(birth_day, now):
    count = 0
    one_day = timedelta(days=1)
    while now != birth_day:
        birth_day += one_day
        count += 1
    return count


time_format = '%m/%d/%Y'
now = datetime.strptime(str(date.today()), '%Y-%m-%d')

if __name__ == '__main__':
    while True:
        birth_day = raw_input("Enter your birday(eg:MM/DD/YYYY):")
        birth_day = datetime.strptime(birth_day, time_format)
        print 'It is %s days from your birth day.' % \
              birday_count(birth_day, now)