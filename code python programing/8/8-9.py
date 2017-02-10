def Fibonacci(num):
    if num in [1, 2]:
        return 1
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)

if __name__ == '__main__':
    for each in xrange(1, 10):
        print each, Fibonacci(each)