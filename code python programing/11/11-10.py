#coding=utf-8\
files = filter(lambda x: x and x[0] != '.', os.listdir(folder))  
#获取非当前目录和父目录的目录内容