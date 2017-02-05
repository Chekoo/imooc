from random import choice

RSP_list = ['R', 'S', 'P']
RSP_dict = {'R':1, 'S': 0,'P':-1}

def Rochambeau(human, pc):
    if RSP_dict[human] == RSP_dict[pc]:
        return 'It is a tie'
    elif RSP_dict[human] - RSP_dict[pc] == 1 or\
        RSP_dict[human] - RSP_dict[pc] == -1:
        return 'You win!'
    else:
        return 'PC win!'



if __name__ == '__main__':
    while True:
        human = (raw_input('R is Rock, S is scissors, P is Paper, enter one of them: ')).upper()
        if human == 'Q':
            break
        else:
            pc = choice(RSP_list)
            print "PC's choice is %s" % pc
            print Rochambeau(human, pc)