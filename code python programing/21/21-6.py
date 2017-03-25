#coding=utf-8

import MySQLdb

ck = MySQLdb.connect(user='root', passwd='ubuntu')
ck.query('drop DATABASE yi')
ck.commit()
ck.close()