#ccoding=utf-8
class StackQueue(object):
    def __init__(self, StackQueue):
        self.StackQueue = StackQueue
    def isEmpty(self):  #当有长度后，not len(x)会返回False
        return (not len(self.StackQueue))
    def shift(self):   #返回并删除第一个元素
        if self.isEmpty():
            print 'empty, can not shift'
        else:
            element = self.StackQueue[0]
            self.StackQueue = self.StackQueue[1:]
            return element
    def unshift(self, element):   #在列表头部“压入“一个新元素
        self.StackQueue = [element] + self.StackQueue
    def push(self, element):  #在列表尾部加上一个新元素
        self.StackQueue.append(element)
    def pop(self):
        self.StackQueue.pop()
    def __str__(self):
        return str(self.StackQueue)
    __repr__ = __str__

if __name__ == "__main__":
    stkque = StackQueue([1, 2, 3])
    print stkque
    print stkque.shift()
    stkque.unshift(6)
    print stkque
    stkque.push(7)
    print stkque
    stkque.pop()
    print stkque