#coding=utf-8
def tr(srcstr, dsrstr, string):
    string_lenth = len(string)
    srcstr_lenth = len(srcstr)
    for i in range(string_lenth):
        if srcstr == string[i:i+srcstr_lenth]:
            new_string = string[0:i] + dsrstr + string[i+srcstr_lenth:]
    return new_string


def tr_low(srcstr, dsrstr, string):
    string_length = len(string)
    srcstr_length = len(srcstr)
    for i in range(string_length):
        if srcstr.lower() ==  string[i:i+string_length].lower():
            new_string = string[0:i] + dsrstr + string[i+srcstr_length:]
    return new_string



if __name__ == '__main__':
    while True:
        srcstr = raw_input('Enter a source word(-1 to quit): ')
        dsrstr = raw_input('Enter a desination word: ')
        string = raw_input('Enter a full string: ')
        swith = raw_input('Case censitive?(Y or N):')#新增
        if srcstr == '-1':
            break
        elif swith.lower() == 'y':
            print tr(srcstr, dsrstr, string)
        elif swith.lower() == 'n':
            print tr_low(srcstr, dsrstr, string)
        else:
            print 'No kidding!'
