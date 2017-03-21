#coding=utf-8

from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}
#TK对话框被关联到按钮回调函数，将在按钮创建时使用它们
critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')
#加载tk,设置标题，并创建了一个quit按钮
top = Tk()
top.title('Road Signs')
Button(top, text='Quit', command=top.quit, bg='red', fg='white').pack()

#模板化的按钮类及根窗口top
MyButton = pto(Button, top)
#使用了上面的结果，mybutton,并再次对它模板化。我们对每个不同的指示类型都创建了单独类型的按钮
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, bg='white')

#遍历指示列表并创建出指示牌
for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
        signType.title(), eachSign,
        '.upper()' if signType == CRIT else '.title()')
    eval(cmd) #对每一个按钮创建字串施以eval()，每次创建一个按钮，最终形成前面看到的图形

top.mainloop()








