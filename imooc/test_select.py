#coding=utf-8
import pymysql

conn = pymysql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '',
    db = 'imooc',
    charset = 'utf8'
)

cursor = conn.cursor()

sql = 'select * from user'
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchall()
for i in rs:
    print 'userid = %s, username = %s' % i

cursor.close()
conn.close()
