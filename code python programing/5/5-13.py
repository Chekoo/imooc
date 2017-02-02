def timetra(time):
    a = time.split(':')
    b = int(a[0]) * 60 + int(a[1])
    return b

timetra('2:10')