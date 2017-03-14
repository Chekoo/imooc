#coding=gbk
import sys
import pymysql


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def check_acct_available(self, acctid):   #查看账号是否存在
        cursor = self.conn.cursor()  #获取游标
        try:
            sql = 'select * from account where acctid=%s' % acctid
            cursor.execute(sql)
            print 'check_acct_aailable:' + sql
            rs = cursor.fetchall()
            if len(rs) != 1:v
                raise Exception('账号%s不存在' % acctid)
        finally:
            cursor.close()   #关闭游标

    def has_enough_money(self, acctid, moeny):  #是否有足够的钱
        cursor = self.conn.cursor()
        try:
            sql = 'select * from account where acctid=%s and money>%s' %(acctid, money)
            cursor.execute(sql)
            print 'has_enough_money:' + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s没有足够的钱' % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):  #扣钱
        cursor = self.conn.cursor()
        try:
            sql = 'update account set money=money-%s where acctid=%s' % (money, acctid)
            cursor.execute(sql)
            print 'reduce_money:' + sql
            if cursor.rowcount != 1:
                raise Exception('账号%s扣款失败' % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):  # 加钱
        cursor = self.conn.cursor()
        try:
            sql = 'update account set money=money+%s where acctid=%s' % (money, acctid)
            cursor.execute(sql)
            print 'add_money:' + sql
            if cursor.rowcount != 1:
                raise Exception('账号%s存款失败' % acctid)
        finally:
            cursor.close()

    def transfer(self, source_acctid, target_acctid, money):   #转账
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()   #回滚事务
            raise e   #抛出异常


if __name__ == '__main__':
    source_acctid = sys.argv[1]   #传入3个参数，分别为转账人，收款人，钱
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = pymysql.Connect(host='localhost', user='root', passwd='', port=3306, database='imooc')  #连接数据库
    tr_money = TransferMoney(conn)    #给类一个conn

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print '出现问题: ' + str(e)
    finally:
        conn.close()   #最后conn必须关闭

