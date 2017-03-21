#coding=utf-8

import Tkinter
from time import ctime

a = ctime()
top = Tkinter.Tk()
label = Tkinter.Label(top, text=a)
label.pack()
Tkinter.mainloop()