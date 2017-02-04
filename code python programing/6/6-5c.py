def check(str):
    n = len(str) - 1
    list = []
    for i in range(n):
        if str[i] == str[i+1]:
            list.append(str[i])
            i += 2
        else:
            i += 1
    return list

if __name__ == '__main__':
    while True:
        str = raw_input('Enter the string')
        if str.lower() == 'q':
            break
        else:
            print check(str)