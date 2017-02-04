def int_to_ip(num):
    W_ = divmod(num, 256 ** 3)
    X_ = divmod(W_[1], 256 ** 2)
    Y_ = divmod(X_[1], 256)
    Z = Y_[1]
    return '.'.join((str(W_[0]), str(X_[0]), str(Y_[0]), str(Z)))

def ip_to_int(ip):
    list = ip.split('.')
    return int(list[0]) * 256 ** 3 + int(list[1]) * 256 * 2 + \
    int(list[2]) * 256 + int(list[3])

if __name__ == '__main__':
    while True:
        int2ip = raw_input('Enter a int(q to quit):')
        if int2ip == 'q':
            break
        else:
            #inta = int(int2ip)
           # print int_to_ip(inta)
            print ip_to_int(int2ip)
