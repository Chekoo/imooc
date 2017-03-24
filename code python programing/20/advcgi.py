#coding=utf-8

from cgi import FieldStorage
from os import environ
from cStringIO import StringIO
from urllib import quote, unquote
from string import capwords, strip, split, join

class AdvCGI(object):
    header = 'Content-Type: text/html\n\n'
    url = 'advcgi.py'

    formhtml = '''
      <html><head><title>Advanced CGI Demo</title></head>
      <body><h2>Advanced CGI Demo Form</h2>
      <form method=post action="%s" enctype="multipart/form-data">
      <h3>My Cookie Setting</h3>
      <li><code><b>CPPuser = %s</b></code>
      <h3>Enter cookie value<br>
      <input name=cookie value="%s">(<I>optional</I>)</h3>
      <h3>Enter your name<br>
      <input name=person value="%s">(<I>required</I>)</h3>
      <h3>What languages can you program in?(<I>at least one required</I>)</h3>
      %s
      <h3>Enter file to upload</h3>
      <input type=file name=upfile value="%s" size=45>
      <p><input type=submit>
      </form></body></html>
    '''

    langSet = ('Python', 'Perl', 'Java', 'C++', 'PHP', 'C', 'JavaScript')

    langItem = '<input type=checkbox name=lang value="%s" %s> %s\n'

    def getCPPCookies(self):  # read cookies from client
        if environ.has_key('HTTP_COOKIE'):
            for eachCookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = unquote(eachCookie[8:])
        else:
            self.cookies['info'] = self.cookies['user'] = ''

        if self.cookies['info'] != '':
            self.who, langStr, self.fn = split(self.cookies['info'], ':')
            self.langs = split(langStr, ',')
        else:
            self.who = self.fn = ' '
            self.langs = ['Python']

    def showForm(self):  # show fill-out form
        self.getCPPCookies()
        langStr = ''
        for eachLang in AdvCGI.langSet:
            if eachLang in self.langs:
                langStr = langStr + AdvCGI.langItem % (eachLang, 'CHECKED', eachLang)
            else:
                langStr = langStr + AdvCGI.langItem % (eachLang, '', eachLang)

        if 'user' not in self.cookies or self.cookies['user'] == '':
            cookieStatus = '<I>(cookie has not been  set yet)</I>'
            userCook = ''
        else:
            userCook = cookieStatus = self.cookies['user']

        print AdvCGI.header + AdvCGI.formhtml % (AdvCGI.url, cookieStatus, userCook, self.who, langStr, self.fn)

    errhtml = '''
    <HTML><HEAD><TITLE>Advanced CGI Demo</TITLE></HEAD>
    <BODY><H3>ERROR</H3>
    <B>%s</B><P>
    <FORM><INPUT TYPE=button VAKUE=Back ONCLICK="window.history.back()"></FORM>
    </BODY></HTML>
    '''

    def showError(self):
        print AdvCGI.header + AdvCGI.errhtml % (self.error)

    reshtml = '''
    <HTML><HEAD><TITLE>Advanced CGI Demo</TITLE></HEAD>
    <BODY><H2>Your Uploaded Data</H2>
    <H3>Your cookie value is: <B>%s</B></H3>
    <H3>Your name is:<B>%s</B></H3>
    <H3>You can program in the following languages:</H3>
    <UL>%s</UL>
    <H3>Your uploaded file...<BR>
    Name:<I>%s</I><BR>
    Contents:</H3>
    <PRE>%s</PRE>
    Click <A HREF="%s"><B>here</B></A> to return to form.
    </BODY></HTML>
    '''

    def setCPPCookies(self):
        for eachCookie in self.cookies.keys():
            print 'Set-Cookie: CPP%s=%s; path=/' % (eachCookie, quote(self.cookies[eachCookie]))

    def doResults(self):
        MAXBYTES = 1024
        langlist = ''
        for eachLang in self.langs:
            langlist = langlist + '<LI>%s<BR>' % eachLang

        filedata = ''
        while len(filedata) < MAXBYTES:
            data = self.fp.readline()
            if data == '':
                break
            filedata = filedata + data
        else:
            filedata = filedata + '...<B><I>(file truncated due to size)</I></B>'
        self.fp.close()
        if filedata == '':
            filedata = '<B><I>(file upload error or file not given)</I></B>'
        filename = self.fn

        if not ('user' in self.cookies and self.cookies['user']):
            cookieStatus = '<I>(cookie has not been set yet)</I>'
            userCook = ''
        else:
            userCook = cookieStatus = self.cookies['user']

        self.cookies['info'] = join([self.who, join(self.langs, ','), filename], ':')
        self.setCPPCookies()
        print AdvCGI.header + AdvCGI.reshtml % (cookieStatus, self.who, langlist, filename, filedata, AdvCGI.url)

    def go(self):  # determine which page to return
        self.cookies = {}
        self.error = ''
        form = FieldStorage()
        if form.keys() == []:
            self.showForm()
            return

        if 'person' in form:
            self.who = capwords(form['person'].value.strip())
            if self.who == '':
                self.error = 'Your name is required. (blank)'
        else:
            self.error = 'Your name is required.(missing)'

        if 'cookie' in form:
            self.cookies['user'] = unquote(form['cookie'].value,strip())
        else:
            self.cookies['user'] = ''

        self.langs = []
        if 'lang' in form:
            langdata = form['lang']
            if isinstance(langdata, list):
                for eachLang in langdata:
                    self.langs.append(eachLang.value)
            else:
                self.langs.append(langdata.value)
        else:
            self.error = 'At least one language required.'

        if 'upfile' in form:
            upfile = form['upfile']
            self.fn = upfile.filename or ''
            if upfile.file:
                self.fp = upfile.file
            else:
                self.fp = StringIO('(no data)')
        else:
            self.fp = StringIO('(no file')
            self.fn = ''

        if not self.error:
            self.doResults()
        else:
            self.showError()

if __name__ == '__main__':
    page = AdvCGI()
    page.go()
