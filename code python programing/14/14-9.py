#coding=utf-8

import os

while True:
    cmd = raw_input('$: ')
    if cmd == 'exit':
        break

    f = os.popen(cmd)
    for line in f:
        print line,
    print