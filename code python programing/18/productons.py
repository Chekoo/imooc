#coding=utf-8
from random import randint
from time import sleep
from Queue import Queue
from time import ctime
import threading

class MyThread(threading.Thread):
    def __init__(self, func, args, name=""):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args
    def getResult(self):
        return self.res
    def run(self):
        print "starting", self.name,"at:",ctime()
        self.res = self.func(*self.args)
        print self.name,"finished at:", ctime()

def writeQ(queue):
    print 'producing object for Q...', queue.put('xxx', 1)
    print 'size now', queue.qsize()

def readQ(queue):
    val = queue.get(1)
    print 'consumed object from Q... size now', queue.qsize()

def write(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))

funcs = [write, reader]
nfuncs = range(len(funcs))
def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in funcs:
        threads[i].join()

    print 'all Done'

if __name__ == '__main__':
    main()