#coding=utf-8
import threading, time
print 'single threading:'
count = 0
timeBegin = time.clock()
for i in range(100):
    with open('data') as fobj:
        for item in fobj:
            count += item.count('os')
timeEnd = time.clock()
print 'os occures:%d' % count
print 'using', (timeEnd - timeBegin), 's'

print 'multiple threading:'
count = 0
def read(count):
    with open('data') as fobj:
        for item in fobj:
            count += item.count('os')

threads = []
timeBegin = time.clock()
for i in range(100):
    t = threading.Thread(target=read, args=(count,))
    threads.append(t)
for i in range(100):
    threads[i].start()
for i in range(100):
    threads[i].join()
tiemEnd = time.clock()
print 'os occures:%d' % count
print 'using', (timeEnd - timeBegin), 's'

