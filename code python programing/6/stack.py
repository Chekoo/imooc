stack = []

def pushit():
    stack.append(raw_input('Enter new string: ').strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed[', `stack.pop()`, ']'

def viewstack():
    print stack

CMDs = {'u': pushit, 'o': popit, 'v': viewstack}

def showmenu():
    show = """
    p(u)sh
    p(o)p
    (V)iew
    (Q)uit

    Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(show).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                break
            CMDs[choice]()

if __name__ == '__main__':
    showmenu()