#coding=utf-8

import os
from time import sleep
from Tkinter import *

class DirList(object):

    def __init__(self, initdir=None):
        self.top = Tk()   #定义了DirList类的构造器以及一个代表我们程序的对象
        self.label = Label(self.top, text='Director Lister v1.1')
        self.label.pack()

        #声明了一个名为cwd的Tk变量来保存当前所在目录的名字
        self.cwd = StringVar(self.top)
        #也创建了另一个标签来显示当前目录的名字
        self.dir1 = Label(self.top, fg='blue', font=('Helevtica', '12', 'bold'))
        self.dir1.pack()
        # dirs(列表框)包含了被列目录的文件列表，使用一个滚动条以便用户在文件数目超过列表
        self.dirfm = Frame(self.top)#窗口尺寸时移动列表，则两个列表包含在一个框架组件中
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50,
                            yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)#列表框用bind把回调函数和列表项绑定起来，双击事件
        self.dirsb.config(command=self.dirs.yview)#贴附在列表框上
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        #创建一个文本框让用户输入用户名,以便转到要去的目录，并在列表框中显示该目录中的文件。
        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLs)#加入一个return或enter键的绑定，这样用户就能
        self.dirn.pack()#敲return的方法代替按钮点击，上面的双击事件也是

        self.bfm = Frame(self.top)  #定义了一个按钮框架来保管clear、go、quit按钮
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
                          activeforeground='white',
                          activebackground='blue')
        self.ls = Button(self.bfm,
                         text='List Directory',
                         command=self.doLs(),
                         activeforeground='white',
                         activebackground='green')
        self.quit = Button(self.bfm, text='Quit',
                           command=self.top.quit,
                           activeforeground='white',
                           activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()
        #初始化了GUI程序，程序将从当前工作目录开始
        if initdir:
            self.cwd.set(os.curdir)
            self.doLs()
    # 清空Tk字符串变量cwd,其中保存当前'活动'目录，这个变量用来跟踪我们当前所处的目录
    def clrDir(self, ev=None):#ev参数缺省值为None,这样任意值都可能由窗口系统传回，在回调函数里可用也可不用
        self.cwd.set('')

    #设置了要到达的目录并产生一个对doLS()的调用，后者负责实现其余的一切。
    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLs()
    #负责所有安全性检查(目标是否是一个目录以及它是否存在?),若发生错误，最终目录会被设置为当前目录。
    def doLs(self, ev=None):#若正确，调用os.listdir()来取得新的文件集合并替换列表框中的列表。
        error = ''
        tdir = self.cwd.get()
        if not tdir: tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return
        #当后台忙于获取新目录信息时，高亮的蓝色会变成红色。当新目录设置完毕，它会恢复蓝色。
        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dir1.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()