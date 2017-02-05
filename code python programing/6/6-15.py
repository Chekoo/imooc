#coding=utf-8


倾向第一种
from datetime import *
# def daysdiff(pre, past):
#     count = 0
#     oneday = timedelta(days=1)
#     while pre != past:
#         pre = pre + oneday
#         count += 1
#     return count
#
# time_format = '%m/%d/%Y'
#
# if __name__ == '__main__':
#     while True:
#         begin_date = raw_input('Enter a begin time(eg:mm/dd/yyyy): ')
#         end_date = raw_input('Enter an end date(eg:mm/dd/yyyy): ')
#         bd = datetime.strptime(begin_date, time_format)
#         ed = datetime.strptime(end_date, time_format)
#         print 'The two time interval is %s day' % daysdiff(bd, ed)

#第二种
def date_convert(date_input):
    month = int(date_input.split('/')[0])
    day = int(date_input.split('/')[1])
    year = int(date_input.split('/')[2])

    return (year,month, day)

date_input = raw_input('Enter a time, MM/DD/YYYY: ')
d1 = date(date_convert(date_input)[0], date_convert(date_input)[1], date_convert(date_input)[2])
date_input = raw_input('Enter a time, MM/DD/YYYY: ')
d2 = date(date_convert(date_input)[0], date_convert(date_input)[1], date_convert(date_input)[2])
print (d2 - d1).days