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

sql_insert = "insert into USER(userid, username) values(10, 'name10') "
sql_update = "update user set username='name91' WHERE userid=9"
sql_delete = "delete from user WHERE  userd < 3"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
except Exception as e:
    print e
    conn.rollback()
conn.commit()
cursor.close()
conn.close()
