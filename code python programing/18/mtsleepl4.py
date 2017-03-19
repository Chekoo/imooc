#coding=utf-8
import threading

from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):  #每个线程都会被分配一个事先已经获得的锁
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops: #实例化一个Thread， 新的线程不会立即开始
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:  #start threads
        threads[i].start()

    for i in nloops: #wait for all， join允许主线程等待线程的结束
        threads[i].join()  #threads to finish

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()