filename = raw_input('Enter a filename: ')
f = open(filename, 'r')
print len([i for i in f])