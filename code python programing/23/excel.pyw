#coding=utf-8

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)


def excel():   # 代码调用Excel后，我们添加了一个工作簿，得到了正在显示的活动表格的句柄
    app = 'Excel'
    x1 = win32.gencache.EnsureDispatch('%s.Application' % app)
    ss = x1.Workbooks.Add()
    sh = ss.ActiveSheet
    x1.Visible = True   # 设置为true，才可以让程序显示在桌面上。
    sleep(1)   # 停顿1秒，为了看见演示过程

    sh.Cells(1,1).Value = 'Python-to-%s Demo' % app
    sleep(1)
    for i in RANGE:
        sh.Cells(i,1).Value = 'Line %d' % i
        sleep(1)
    sh.Cells(i+2,1).Value = "Th-th-th-that's all folks!"

    warn(app)
    ss.Close(False)
    x1.Application.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    excel()
