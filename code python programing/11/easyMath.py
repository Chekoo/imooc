#coding=utf-8
from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2

def doprob():  #随机选择一个操作并生成两个操作数，为了避免减法问题中的负数问题，将这两个算子按大到小进行排序，然后用值调用一个数学函数，计算出正确答案
    op = choice('+-')    #用一个等式来提示用户输入并给用户3次机会来输入一个正确的答案。
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d=' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input... try again'


def main():
    while True:
        doprob()

        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()