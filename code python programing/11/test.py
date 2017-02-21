#coding=utf-8
@decorator(dec_opt_args)
def func2Bdecorated(func_opt_args):
	
def map(func, seq):
	mapped_seq = []
	for eachItem in seq:
		mapped_seq.append(func(eachItem))
	return mapped_seq

def reduce(bin_func,seq,init=None):
	lseq = list(seq)
	if init is None:
		res = lseq.pop(0)
	else:
		res = init
	for item in lseq:
		res = bin_func(res, item)
	retrun res

from functools import partial
import Tkinter

root = Tkinter.Tk()
#给Tkinter.Button创建了部分类实例化器，固定好父类的窗口参数然后是前景色和背景色。创建了b1,b2来与模板匹配，只让文本标签唯一。quit配置了一个回调的函数，当按钮被按下，关闭窗口
MyButton = partial(Tkinter.Button, root, fg = 'white', bg = 'blue')	    
b1 = MyButton(text='Button1')
b2 = MyButton(text='Button2')
qb = MyButton(text='QUIT', bg='red', command=root.quit)

b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()