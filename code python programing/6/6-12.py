#coding=utf-8
def findchr(string, char):
    slen = len(string)
    clen = len(char)
    for i in range(slen - clen + 1):
        if char == string[i:i+clen]:
            return i
        else:
            continue
    return -1

#b
def findchr(string, char):
    slen = len(string)
    for i in range(-1, -slen, -1):
        if char == string[i]:
            return slen + i
        else:
            continue
    return -1

#c
def subchr(string, orichar, newchar):
    string_list = list(string)
    string_lenth = len(string)
    for i in range(string_lenth):
        if orichar == string_list[i]:
            string_list[i] = newchar
    return ''.join(string_list)

#c可用

if __name__ == '__main__':
    while True:
        string = raw_input('string ,-1 to quit')
        orichar = raw_input('orichar')
        newchr = raw_input('newchar')
        if string == '-1':
            break
        else:
            print subchr(string, orichar, newchr)



#a、b可用
# if __name__ == '__main__':
#     while True:
#         string = raw_input('string ,q to quit')
#         char = raw_input('char, q to quit')
#         if string == 'q' or char == 'q':
#             break
#         else:
#             print findchr(string, char)

