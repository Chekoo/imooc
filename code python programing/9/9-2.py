filename = raw_input('Enter filename: ')
num = int(raw_input('Enter the number: '))

for each in open(filename):
    if num:
        print each,
        num -= 1
    else:
        break