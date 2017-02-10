if __name__ == '__main__':
    dict1 = {}
    while True:
        list1 = []
        name_num = raw_input("Please input a dicy key-value pair, like'a:1'('E' to end enroll)")
        if name_num.lower() == 'e':
            word = raw_input("Array it by name(for '1') or number(for '2')?:")
            break
        else:
            list1 = name_num.split(':')
            dict1[list1[0]] = list1[1]
    if word == '1':
        for key in sorted(dict1):
            print key, dict1[key]
    elif word == '2':
        for i in sorted(dict1.values()):
            for key in dict1:
                if dict1[key] == i:
                    print i, key
    else:
        print 'Wrong!'
