def getfactors(num):
    list1 = [1]
    for i in range(1, num + 1):
        if num % 2 == 0:
            list1.append(2)
            num = num / 2
        else:
            list1.append(num)
            break
    return list1

def isperfect(num):
    if sum(getfactors(num)) == num:
        return 1
    else:
        return 0

if __name__ == '__main__':
    while True:
        num = int(raw_input('Enter a number: '))
        print isperfect(num)