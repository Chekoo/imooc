fobj1 = open('hello.txt')
fobj2 = open('note.txt')
line1 = fobj1.readline()
line2 = fobj2.readline()
for i in range(min(len(line1), len(line2))):
    if line1[i] != line2[i]:
        print i
        break

