#coding=utf-8
#普通版本
# def change(str):
#     dic = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
#            '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten'}
#     result = ''
#     for i in str:
#         result += dic[i] + '-'
#     print result[:-1]
#
# if __name__ == '__main__':
#     str = raw_input()
#     print change(str)

#附加题
def change(str):
    dic_unit = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
            '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten'}
    dic_decade = {'11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen',
            '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty'}
    dic_decade2 = {'2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty',
                   '7':'seventy', '8':'eighty', '9':'ninety'}
    num = int(str)
    result = ""

#这个函数专门处理21到99
    def ninenine(mynum):
        myresult = dic_decade2[mynum[0]] + '-' + dic_unit[mynum[1]]
        return myresult

    if num > 1000:
        print 'Please enter a number less than 1000'
        return

    if num < 11:
        result = dic_unit[str]
    elif num < 21:
        result = dic_decade[str]
    elif num < 100:
        result = ninenine(str)
    else:
        result = dic_unit[str[0]] + 'hundred-' + ninenine(str[1:])
    print result


if __name__ == '__main__':
    while True:
        string = raw_input('enter the number: ')
        if string == 'q':
            break
        else:
            print change(string)
