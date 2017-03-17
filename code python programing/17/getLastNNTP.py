#coding=utf-8

import nntplib
import socket

HOST = 'your.nntp.server'
GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = "you'llNeverGuess"

def main():
    try:
        n = nntplib.NNTP(HOST)
        user = USER,  password = PASS
    except socket.gaierror, e:
        print 'ERROR: cannot reach host "%s"' % HOST
        print '("%s")' % eval(str(e))[1]
        return
    except nntplib.NN