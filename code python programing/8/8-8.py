def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

if __name__ == '__main__':
    for each in xrange(1, 10):
        print each, fact(each)