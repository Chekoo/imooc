def atoc(string):
    strlen = len(string)
    for i in range(strlen-2, 0, -1):
        if string[i] in ['+', '-']:
            print i
            return complex(float(string[0:i]),float(string[i:strlen-1]))


def atocc(input):
    real = complex(input).real
    imag = complex(input).imag
    print 'complex real is:', real
    print 'complex imag is:', imag

if __name__ == '__main__':
    while True:
        str = raw_input('str,q to quit: ')
        if str == 'q':
            break
        else:
            print atoc(str)