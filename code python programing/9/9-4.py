with open('hello.txt') as fobj:
    num = 1
    for each in fobj:
        if num - 26 != 0:
            print each,
            num += 1
        else:
            go = raw_input('continue(c to continue, other to quit): ').lower()
            num += 1
            if go != 'c':
                break
fobj.close()