def isprime(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            return False
            break
        count -= 1
    else:
        print 'It is prime'
        return True

if __name__ == '__main__':
    while True:
        num = int(raw_input('Enter a number: '))
        print isprime(num)
