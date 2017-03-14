#coding=gbk
import sys
import pymysql


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def check_acct_available(self, acctid):   #�鿴�˺��Ƿ����
        cursor = self.conn.cursor()  #��ȡ�α�
        try:
            sql = 'select * from account where acctid=%s' % acctid
            cursor.execute(sql)
            print 'check_acct_aailable:' + sql
            rs = cursor.fetchall()
            if len(rs) != 1:v
                raise Exception('�˺�%s������' % acctid)
        finally:
            cursor.close()   #�ر��α�

    def has_enough_money(self, acctid, moeny):  #�Ƿ����㹻��Ǯ
        cursor = self.conn.cursor()
        try:
            sql = 'select * from account where acctid=%s and money>%s' %(acctid, money)
            cursor.execute(sql)
            print 'has_enough_money:' + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('�˺�%sû���㹻��Ǯ' % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):  #��Ǯ
        cursor = self.conn.cursor()
        try:
            sql = 'update account set money=money-%s where acctid=%s' % (money, acctid)
            cursor.execute(sql)
            print 'reduce_money:' + sql
            if cursor.rowcount != 1:
                raise Exception('�˺�%s�ۿ�ʧ��' % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):  # ��Ǯ
        cursor = self.conn.cursor()
        try:
            sql = 'update account set money=money+%s where acctid=%s' % (money, acctid)
            cursor.execute(sql)
            print 'add_money:' + sql
            if cursor.rowcount != 1:
                raise Exception('�˺�%s���ʧ��' % acctid)
        finally:
            cursor.close()

    def transfer(self, source_acctid, target_acctid, money):   #ת��
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()   #�ع�����
            raise e   #�׳��쳣


if __name__ == '__main__':
    source_acctid = sys.argv[1]   #����3���������ֱ�Ϊת���ˣ��տ��ˣ�Ǯ
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = pymysql.Connect(host='localhost', user='root', passwd='', port=3306, database='imooc')  #�������ݿ�
    tr_money = TransferMoney(conn)    #����һ��conn

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print '��������: ' + str(e)
    finally:
        conn.close()   #���conn����ر�

