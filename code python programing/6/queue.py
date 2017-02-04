queue = []

def enq():
        queue.append(raw_input('Enter the new string: '))

def outq():
    if len(queue) == 0:
        print 'This is error'
    else:
        print 'Remove [', `queue.pop(0)`, ']'

def viewq():
    print queue

cmd = {'e': enq, 'o': outq, 'v': viewq}

def showmenu():
    some = '''
    e: enter
    o: out
    v: view
    q: quit
    Enter choice:
    '''


    while True:
        while True:
            try:
                choice = raw_input(some).strip().lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print 'You pick[%s]' % choice
            if choice not in 'eovq':
                break
            else:
                cmd[choice]()

if __name__ == '__main__':
    showmenu()