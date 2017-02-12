with open('hello.txt') as fobj:
    for each in fobj:
        if not each.startswith('#'):
            print each