#coding=utf-8
print u'输入的格式是姓-名,中间用英文逗号隔开'
namenum = int(raw_input(u'输入名字个数： ').encode('gbk'))

names = []
errors = 0
for i in range(namenum):
    prompt = u'请输入第%d 个姓-名' % i
    ai = raw_input(prompt)
    if ',' not in ai:
        errors += 1
        print u'格式输错了%d次,请注意！' % errors
        names.append(ai.replace(' ', ','))
    else:
        names.append(ai)

print u'按照姓氏排序后输入的姓名如下：'
for name in names:
    print ' ' * 4, name