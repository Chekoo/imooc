def check(str):
    new1 = list(str)
    new1.reverse()
    new2 = list(str) + new1
    return ''.join(new2)


if __name__ == '__main__':
    while True:
        str = raw_input('Enter the string, q to quit')
        if str.lower() == 'q':
            break
        else:
            print check(str)