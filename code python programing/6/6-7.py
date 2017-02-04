#coding=utf-8

#采集一个数字
num_str = raw_input('Enter a number: ')

#将采集的数字变成数值
num_num = int(num_str)

#<=这个数值的所有正整数罗列出来
fac_list = range(1, num_num+1)
list = fac_list[:]
print 'BEFORE:', fac_list


#先print出来
i = 0

while i < len(fac_list):

    if num_num % fac_list[i] == 0:
        list.remove(fac_list[i])

#原意是想去掉所有能被这个整除的数字
    i += 1

print 'AFTER:', list