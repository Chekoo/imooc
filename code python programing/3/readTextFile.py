# get filename
fname = raw_input('Enter filename: ')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open erroe:", e
else:
    # display contents to the screen
    for eachLine in fobj:
       # print eachLine,
        print eachLine.strip()
    fobj.close()