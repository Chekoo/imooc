def print_string(begin_num, end_num):
    begin_num = min(begin_num, end_num)
    end_num = max(begin_num, end_num)
    if begin_num > 127 or end_num < 33:
        print 'DEC\t\tBIN\t\tOCT\t\tHEX'
        print '-' * 30
    else:
        print 'DEC\t\tBIN\t\tOCT\t\tHEX\t\tASCII'
        print '-' * 40
    for x in xrange(begin_num, end_num+1):
        if 32 < x <127:
            print '%-8d%-8d%-8o%-8x%-8c' % (x, int(bin(x)[2:]), x, x, x)
        else:
            print '%-8d%-8d%-8o%-8x' % (x, int(bin(x)[2:]), x, x)
print_string(27, 41)