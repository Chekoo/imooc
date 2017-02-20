def safe_open(name = None, mode = 'r'):
    try:
        f = open(name, mode)
    except IOError:
        f = None
    else:
        return f

if __name__ == '__main__':
    f = safe_open('1.txt')
    print f