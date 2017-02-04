def del_space(str):
    str = list(str)
    i = 0
    lenth = len(str)
    while str[0] == ' ':
        str.pop(0)
    while str[-1] == ' ':
        str.pop()
    return ''.join(str)

if __name__ == '__main__':
    while True:
        str = raw_input('Enter a string, q to quit: ')
        if str == 'q':
            break
        else:
            print del_space(str)