from datetime import *
import time
def date_convert(date_input):
    month = int(date_input.split('/')[0])
    day = int(date_input.split('/')[1])
    year = int(date_input.split('/')[2]) + 1

    return (year,month, day)

date_input = raw_input('Enter a time, MM/DD/YYYY: ')
next_birthday = date(date_convert(date_input)[0], date_convert(date_input)[1], date_convert(date_input)[2])
a =  (next_birthday - date.today()).days
if a >= 365:
    a -= 365
    print a
else:
    print a
