import os
ls = os.linesep

def write():
    # get filename
    while True:
        fname = raw_input('> ')
        if os.path.exists(fname):
            print "ERROR: '%s' already exists" %fname
        else:
            break

    # get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"

    # loop untile user terminates input
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines({'%s%s' % (x, ls) for x in all})
    fobj.close()
    print 'Done!'

def read():
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

if __name__ == "__main__":
    while True:
        print "1.write\n2.read\n3.quit"
        a = raw_input('> ')
        if a == '1':
            write()
        elif a == '2':
            read()
        elif a == '3':
            break
        else:
            print "Please input 1 or 2"