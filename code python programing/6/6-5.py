def output(str):
    n = len(str)
    aList = []
    if n % 2 == 0:
        for i in range(0, n/2):
            aList.append(str[i])
            aList.append(str[n-i-1])
        else:
            for i in range(0, int(n/2)+1):
                if i != int(n/2):
                    aList.append(str[i])
                    aList.append(str[n-i-1])
                else:
                    aList.append(str[int(n/2)])

    return aList

if __name__ == '__main__':
    str = raw_input('Enter something')
    print output(str),