def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval

try:
    try:
        ccfile = open('carddata.txt', 'r')
        txns = ccfile.readlines()
    except IOError:
        log.write('no txns this month\n')
finally:
    ccfile.close()




if __name__ == '__main__':
    print safe_float('xyz')
    print safe_float('bad input')
    print safe_float(())