#coding=utf-8
from Tix import *
from Tkinter import Label, Button, END
from Tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('package require Tix')

#创建label
lb = Label(top, text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()
#创建控制
ct = Control(top, label='Number:', integer=True, max=12, min=2, value=2, step=2)
ct.label.config(font='Helvetica -14 bold')
ct.pack()
#创建组合框
cb = ComboBox(top, label='Type', editable=True)
for animal in ('dog', 'cat', 'hamster', 'python'):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text='Quit', command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()