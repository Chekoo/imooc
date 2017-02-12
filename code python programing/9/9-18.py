fileName = raw_input('please enter the fileName: ')
fileCh = raw_input('please enter the character: ')
countNum = 0
with open(fileName) as fobj:
    for i in fobj:
        countNum += i.count(fileCh)
print 'character %s occurs: %d' % (fileCh, countNum)