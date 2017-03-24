#coding=utf-8

from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO

#负责从web上下载页面，解析每个文档中的连接并在必要的时候把它们加入todo队列。
#我们为每个从网上下载的页面都查收能见一个Retriever类的实例。


class Retriever(object):    # download Web Page,检索并解析每一个下载的web页面
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, deffile='index.php'):
        parsedurl = urlparse(url, 'http:', 0)  # parse path
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        if ext[1] == '':   # no file, use default
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
        ldir = dirname(path)  # local directory
        if sep != '/':    # os-indep.path separator
            ldir = replace(ldir, '/', sep)
        if not isdir(ldir):   # create archive dir if nec.
            if exists(ldir): unlink(ldir)
            makedirs(ldir)
        return path

    def download(self):  # download web page
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL"%s"' % self.url)
            return retval

    def parseAndGetLinks(self):  # parse HTML, save links,解析新下载的页面并决定该页面中每个链接的后续动作
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist


# manage entire crawing process
class Crawler(object):
    count = 0  # 每一个页面成功下载它就会增加1

    def __init__(self, url):
        self.q = [url]    # 一个待下载链接的队列
        self.seen = []    # 我们已看过，已下载的链接的列表和dom，我们把主链接的域名存在这里，并用这个值来判定后续链接是否是该域的一部分
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*':  # error situation, do not parse
            print retval, '... skipping parse'
            return
        Crawler.count += 1
        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', retval[0]
        self.seen.append(url)

        links = r.parseAndGetLinks()  # get and process links
        for eachLink in links:
            if eachLink[:4] != 'http' and find[eachLink, '://'] == -1:
                eachLink = urljoin(url, eachLink)
            print '* ', eachLink,

            if find(lower(eachLink), 'mailto:') != -1:
                print '... discrded, mailto link'
                continue

            if eachLink not in self.seen:
                if find(eachLink, self.dom) == -1:
                    print '...discarded, not in domain'
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print '... new, added to Q'
                    else:
                        print '... discarded, already in Q'
            else:
                print '... discarded, already processed'

    def go(self):   # process links in queue
        while self.q:
            url = self.q.pop()
            self.getPage(url)

def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = raw_input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''
    if not url:
        return
    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()