def swap(list1):
    lenth = len(list1)
    list = []
    for i in range(lenth):
        if 65 <= ord(list1[i]) <= 90:
            list.append(chr(ord(list1[i]) + 32))
        elif 97 <= ord(list1[i]) <= 122:
            list.append(chr(ord(list1[i]) - 32))
        else:
            list.append(list1[i])
    return "".join(list)

if __name__ == '__main__':
    while True:
        string = raw_input('enter the string ,q to quit')
        if string == 'q':
            break
        else:
            list1 = list(string)
            print swap(list1)