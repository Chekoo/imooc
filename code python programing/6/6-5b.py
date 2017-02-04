def bi(str1, str2):
    a = list(str1)
    b = list(str2)
    if len(a) != len(b):
        return 'They do not match'
    else:
        n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            return 'They do not match'
        else:
            if i != n-1:
                continue
            else:
                return 'They match.'


if __name__ == '__main__':
    str1 = raw_input('Enter a string')
    str2 = raw_input('Enter a string')
    print bi(str1, str2)