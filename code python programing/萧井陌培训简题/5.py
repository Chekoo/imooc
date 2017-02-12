#coding=utf-8
# 题 5
# 写一个 Queue 类，它有两个方法，用法如下
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3


class Queue(object):
    def __init__(self):
        self.list = []
    def enqueue(self, mem):
        self.list.append(mem)
    def dequeue(self):
        if len(self.list) != 0:
            return self.list.pop(0)