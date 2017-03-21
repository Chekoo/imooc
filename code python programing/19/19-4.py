#coding=utf-8

import Tkinter
from tkMessageBox import showinfo, showwarning, showerror

top = Tkinter.Tk()

hello = Tkinter.Label(top, text='Hello World!')
hello.pack()
hello = lambda: showerror('Error', 'hello')
world = lambda: showinfo('Error', 'world!')
hi = lambda: showwarning('Error', 'hi!')

quit = Tkinter.Button(top, text='Quit', command=top.quit, bg='red', fg='white')
quit.pack(fill=Tkinter.X, expand=6)  #x为横放，默认为垂直

hello = Tkinter.Button(top, text='hello', command=hello, bg='black', fg='white')
hello.pack(fill=Tkinter.X, expand=6)  #x为横放，默认为垂直

world = Tkinter.Button(top, text='world', command=world, bg='green', fg='white')
world.pack(fill=Tkinter.X, expand=6)  #x为横放，默认为垂直

hi = Tkinter.Button(top, text='hi', command=hi, bg='blue', fg='white')
hi.pack(fill=Tkinter.X, expand=6)  #x为横放，默认为垂直

Tkinter.mainloop()
