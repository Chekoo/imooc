def cal(set_A, set_B, op):
    return eval(str(set_A) + str(op) + str(set_B))

if __name__ == "__main__":
    A = raw_input('Enter the first set, like:1, 2, 3(q to quit): ')
    B = raw_input('Enter the second set, like:1, 2, 3: ')
    option = raw_input('Enter option you want: ')
    A = set(A.split(','))
    B = set(B.split(','))
    print '%s,%s,%s is %s.' % (A, option, B, cal(A, B, option))