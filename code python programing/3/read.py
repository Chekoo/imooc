#coding=utf-8
fname = raw_input('> ')
try:
    doc = open(fname, 'r')
except IOError, e:
    print "ERROR: ", e
else:
    for li in doc:
        print li,
    doc.close()