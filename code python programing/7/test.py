db = {}

def newuser():
    prompt = 'enter the username'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            print 'please input another name,the name is exist: '
        else:
            break

    pwd = raw_input('password: ')
    db[name] = pwd

def olduser():
    name = raw_input('enter username: ')
    pwd = raw_input('enter password: ')
    pasd = db.get(name)
    if pwd == pasd:
        print 'Welcome come back, %s' % name
    else:
        print 'enter right password'


def showmenu():
    pop = '''
    (N)ew user
    (L)ogin
    (Q)uit
    Enter choice:
    '''
    turn = False
    while not turn:
        try:
            ch = raw_input(pop)
            choice = ch.strip()[0].lower()
        except(EOFError, KeyboardInterrupt):
            choice = 'q'
        print 'You pick [%s]' % choice
        if choice not in 'nlq':
            print 'Error,try again'
        else:
            turn = True


        if choice == 'n': newuser()
        if choice == 'l': olduser()
        if choice == 'q': turn = True



if __name__ == '__main__':
    showmenu()