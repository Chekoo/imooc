#coding=utf-8
#HTTP认证客户端
import urllib2

LOGIN = 'wesc'
PASSWD = "you'llNeverGuess"
URL = 'http://localhost'

def handler_version(url):
    from urlparse import urlparse as up
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', up(url)[1], LOGIN, PASSWD)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url
#创建了一个Request对象，并在http请求中添加了基本的base64编码认证头信息。
def request_version(url):
    from base64 import encodestring
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
    req.add_header('Authorization', 'Basic %s' % b64str)
    return req

#用两种技术分别打开了给定的URL，并显示服务器返回的HTML页面第一行。
for funcType in ('handler', 'request'):
    print '*** Using %s:' % funcType.upper()
    url = eval('%s_version')(URL)
    f = urllib2.urlopen(url)
    print f.readline()
    f.close()