#coding=utf-8

from socket import *
from time import ctime

HOST = ''   #HOST变量为空，表示bind()可以绑定在所有有效低智商
PORT = 21567
BUFSIZ = 1024   #缓冲区大小为1K
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)   #生成TCP服务套接字
tcpSerSock.bind(ADDR)   #绑定到服务器地址 ，然后开始TCP监听
tcpSerSock.listen(5)   #listen参数只是表示最多允许多少个连接同时连进来，后来的连接会拒绝


while True:   #等待连接到来，有连接时候进入对话循环
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))
        tcpCliSock.close()
tcpSerSock.close()