#coding=utf-8

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError, e:
        log.write('no txns this month\n')
        log.close()
        return

    #1.读入信用卡数据文件  2.处理输入  3.显示结果
    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for each in txns:
        result = safe_float(each)
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')
        else:
            log.write('ignored: %s' % result)
    print '$%.2f (new balance)' % (total)
    log.close()

if __name__ == '__main__':
    print main()
