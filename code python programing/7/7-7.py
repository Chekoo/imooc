def swap(dct):
    change = {}
    for key in dct:
        change[dct[key]] = key
    return change

if __name__ == '__main__':
    while True:
        dict1 = input('Please input a dict(-1 to quit): ')
        if dict1 == -1:
            break
        else:
            print swap(dict1)
