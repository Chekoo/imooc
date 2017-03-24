#coding=utf-8

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''<html><head><title>
Friends CGI Demo</title></head>
<body><h3>Friends list for: <I>New User</I></h3>
<form action="friends2.py">
<B>Enter your name:</B>
<input type=hidden name=action value=edit>
<input type=text name=person value="new user" size=15>
<P><B>How many friends do you have?</B>
%s
<P><input type=submit></form></body></html>'''

fradio = '<input type=radio name=howmany value="%s" %s> %s\n'

def showForm():  #负责对用户输入生成表单页
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if i == 0:
            checked = 'CHECKED'
        friends = friends + fradio % (str(i), checked, str(i))

    print header + formhtml % (friends)

reshtml = '''
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

def doResults(who, howmany):
    print header + reshtml % (who, who, howmany)

def process():
    form = cgi.FieldStorage()
    if form.has_key('person'):
        who = form['person'].value
    else:
        who = 'NEW USER'

    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        howmany = 0

    if form.has_key('action'):
        doResults(who, howmany)
    else:
        showForm()

if __name__ == '__main__':
    process()