#coding=utf-8

from Tkinter import Tk
from time import sleep, ctime
from tkMessageBox import showwarning
from urllib import urlopen
import win32com.client as win32


warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)
TICKS = ('YHOO', 'GOOG', 'EBAY', 'AMZN')
COLS = ('TICKER', 'PRICE', 'CHG', '%AGE')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sllclp2'

def excel():
    app = 'Excel'
    x1 = win32.gencache.EnsureDispatch('%s.Application' % app)
    ss = x1.Workbooks.Add()
    sh = ss.ActiveSheet
    x1.Visible = True
    sleep(1)

    sh.Cells(1,1).Value = 'Python-to-%s Stock Quote Demo' % app
    sleep(1)
    sh.Cells(3,1).Value = 'Prices quoted as of: %s' % ctime()
    sleep(1)
    for i in range(4):
        sh.Cells(5, i+1).Value = COLS[i]
    sleep(1)
    sh.Range(sh.Cells(5, 1), sh.Cells(5, 4)).Font.Bold = True
    sleep(1)
    row = 6

    u = urlopen(URL % ','.join(TICKS))
    for data in u:
        tick, price, chq, per = data.split(',')
        sh.Cells(row, 1).Value = eval(tick)
        sh.Cells(row, 2).Value = ('%.2f' % round(float(price), 2))
        sh.Cells(row, 3).Value = chq
        sh.Cells(row, 4).Value = eval(per.rstrip())
        row += 1
        sleep(1)
    f.close()

    warn(app)
    ss.Close(False)
    x1.Application.Quit()

if __name__ == "__main__":
    Tk().withdraw()
    excel()