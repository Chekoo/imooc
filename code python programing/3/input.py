#coding=gbk
import os
ls = os.linesep



#�鿴�ļ��Ƿ����
while True:
    fname = raw_input('> ')
    if os.path.exists(fname):
        print "Error�� %s is already exist "  %fname
    else:
        break

#��������
all = []
print "\nentry '.' to end\n"

while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)


#������д���ĵ�
doc = open(fname, 'w')
doc.writelines({'%s%s' % (x, ls) for x in all})   #lsΪ\n
doc.close()