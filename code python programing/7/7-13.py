from random import *
def gen_num(s):
    for i in range(10):
        s.add(str(randint(0, 9)))
    return s

if __name__ == '__main__':
    A = set()
    B = set()
    gen_num(A)
    gen_num(B)
    print 'A is %s.' % A
    print 'B is %s.' % B
    union_AB = (A|B)
    intersection_AB = (A&B)
    i = 0
    while i < 3:
        user_input = raw_input("Try to enter the union of the two(',' to divide): ")
        user_union = set(user_input.split(','))
        if union_AB == user_union:
            print 'You are so great!'
            break
        else:
            if i <= 1:
                print 'Try again!'
                i += 1
                print i
            else:
                print 'You lose!'
                print 'The answer is %s.' % union_AB
                i += 1
