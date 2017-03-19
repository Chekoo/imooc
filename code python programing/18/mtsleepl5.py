#coding=utf-8
import threading

from time import sleep, ctime


loops = (4, 2)

class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)#子类构造器一定要先调用基类的构造器
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        apply(self.func, self.args)

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops: #create all threads,
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:  # start all threads
        threads[i].start()

    for i in nloops: #wait for all， join允许主线程等待线程的结束
        threads[i].join()  #threads to finish

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()