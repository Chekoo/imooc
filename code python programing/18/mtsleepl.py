#coding=utf-8
import thread

from time import sleep, ctime

loops = [4, 2]
def loop(nloop, nsec, lock):  #每个线程都会被分配一个事先已经获得的锁
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()#在sleep()时间到了之后就释放相应的锁以通知主线程，这线程结束

def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()#创建锁的列表
        lock.acquire()#获得锁
        locks.append(lock)#把锁放到锁列表locks中

    for i in nloops:#创建线程，每个线程都用各自的循环号
        thread.start_new_thread(loop, (i, loops[i], locks[i])
                                )
    for i in nloops:#直到两个锁都被解锁为止才继续运行
        while locks[i].locked(): pass

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()