def rot13(string):
    string_length = len(string)
    list1 = list(string)
    list_empty = []
    for i in range(string_length):
        if 97 <= ord(list1[i]) <= 109 or 65 <= ord(list1[i]) <= 77:
            list_empty.append(chr(ord(list1[i])+13))
        elif 110 <= ord(list1[i]) <= 122 or 78 <= ord(list1[i]) <= 90:
            list_empty.append(chr(ord(list1[i])-13))
        else:
            list_empty.append(list1[i])
    return ' '.join(list_empty)

if __name__ == '__main__':
    while True:
        string_ori = raw_input('Enter a string to en rot13(q to quit): ')
        if string_ori == 'q':
            break
        else:
            print 'You string to en/decrypt was:[%s].' % string_ori
            swithch = raw_input('En/decrypt?[E/D]: ')
            if swithch.lower() == 'e' or swithch.lower() == 'd':
                print rot13(string_ori)
            else:
                print 'Wrong choose!'