#coding=utf-8
import os
from random import randrange as rrange

COLSIZ = 10
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g': 'gadfly'}
DB_EXC = None  # 代表数据库异常


def setup():  # 提供一个简单界面让用户选择哪种数据库
    return RDBMSs[raw_input('''
    Choose a database system:
    (M)ySQL
    (Q)adfly
    (S)QLite''').strip().lower()[0]]


def connect(db, dbName):  # 数据库连接建立后，其余的代码对数据库和接口程序来说都是透明的。
    global DB_EXC
    dbDir = '%s_%s' % (db, dbName)

    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError, e:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError, e:
                return None

        DB_EXC = sqlite3    # sqlite3是基于文件的数据库系统
        if not os.path.isdir(dbDir):  # 确认下数据库文件所在的目录是否存在
            os.mkdir(dbDir)
        cxn = sqlite3.connect(os.path.join(dbDir, dbName))

    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC
        except ImportError, e:
            return None

        try:
            cxn = MySQLdb.connect(db=dbName)
        except DB_EXC.OperationalError, e:
            cxn = MySQLdb.connect(user='root', passwd='ubuntu')
        try:
            cxn.query('DROP DATABASE %s' % dbName)
        except DB_EXC.OperationalError, e:
            pass
        cxn.query('CREATE DATABASE %s' % dbName)
        #cxn.query("GRANT ALL ON %s.* to ''@'localhost'" % dbName)
        #cxn.query('FLUSH PRIVILEGES;')
        cxn.commit()
        cxn.close()
        cxn = MySQLdb.connect(db=dbName, user='root', passwd='ubuntu')

    elif db == 'gadfly':
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except ImportError, e:
            return None
        try:
            cxn = gadfly(dbName, dbDir)
        except IOError, e:
            cxn = gadfly()
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            cxn.startup(dbName, dbDir)
        else:
            return None
    return cxn


def create(cur):
    try:
        cur.execute('''CREATE TABLE users (
        login VARCHAR(8),
        uid INTEGER,
        prid INTEGER)
        ''')
    except DB_EXC.OperationalError, e:
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
    ('aaron', 8312), ('angela', 7603), ('dave', 7306),
    ('davina', 7902), ('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209)
)


def randName():  # NAMES常量是一个元组，必须将它转化成list
    pick = list(NAMES)   # 如果NAMES本身是一个列表，我们只能使用它一次就被消耗光了
    while len(pick) > 0:
        yield pick.pop(rrange(len(pick)))


def insert(cur, db):  # 对每个name-userID数据对，随机分配一个项目小组ID，然后存入数据库
    if db == 'sqlite':
        cur.executemangy("INSERT INTO users VALUES(?, ?, ?)",
                         [(who, uid, rrange(1, 5)) for who, uid in randName()])
    elif db == 'gadfly':
        for who, uid in randName:
            cur.execute("INSERT INTO users VALUES(?, ?, ?)",
                        (who, uid, rrange(1, 5)))
    elif db == 'mysql':
        cur.executemany('INSERT INTO users VALUES(%s, %s, %s)',
                        [(who, uid, rrange(1, 5)) for who, uid in randName()])

# 返回最后一步操作所影响的行数。 如果游标对象不支持这个属性，它返回-1
getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1


def update(cur):  # 随机从一个组选择几条记录，如果是udpate操作，将它们从当前小组移到另一个小组(也是随机选择)
    fr = rrange(1, 5)
    to = rrange(1, 5)
    cur.execute("UPDATE users SET prid=%d WHERE prid=%d" % (to, fr))
    return fr, to, getRC(cur)


def delete(cur):  # 跟update一样，不过是删除它们
    rm = rrange(1, 5)
    cur.execute('DELETE FROM users WHERE prid=%d' % rm)
    return rm, getRC(cur)


def dbDump(cur):  # 从数据库中读取所有数据，并将数据进行格式化，然后显示给用户看。
    cur.execute('SELECT login, uid, prid FROM users')
    print '\n%s%s%s' % ('LOGIN'.ljust(COLSIZ),
                        'USERID'.ljust(COLSIZ),
                        'PROJ#'.ljust(COLSIZ))
    for data in cur.fetchall():  # 通过fetchall()读取数据，然后迭代遍历每个用户.将三列数据
        print '%s%s%s' % tuple([str(s).title().ljust(COLSIZ) for s in data])
                                 # 转换为字符串，并将姓和名首字母大写,再格式化整个字符为左对齐的COLSIZ列。由代码生成的字符串是列表，我们将它们转化成一个元组以支持%操作符


def main():
    db = setup()
    print '*** Connecting to %r database' % db
    cxn = connect(db, 'test')

    if not cxn:
        print 'ERROR: %r not supported, exiting' % db
        return
    cur = cxn.cursor()

    print '\n*** Creating users table',
    create(cur)

    print '\n*** Inserting names into table',
    insert(cur, db)
    dbDump(cur)

    print '\n*** Randomly choosing group.',
    rm, num = delete(cur)
    print '(%d) to delete' % rm
    print '\t(%d users removed)' % num
    dbDump(cur)

    print '\n*** Drop users table'
    drop(cur)
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == "__main__":
    main()