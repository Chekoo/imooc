#coding=gbk
import os
ls = os.linesep



#查看文件是否存在
while True:
    fname = raw_input('> ')
    if os.path.exists(fname):
        print "Error： %s is already exist "  %fname
    else:
        break

#输入内容
all = []
print "\nentry '.' to end\n"

while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)


#将内容写入文档
doc = open(fname, 'w')
doc.writelines({'%s%s' % (x, ls) for x in all})   #ls为\n
doc.close()