#coding=utf-8
import time
import wx
import string

class UserPw(object):
    '''登录系统的类，包含用户登录,超级用户删除用户，显示所有用户
    (需要超级用户账号和密码)'''

    def __init__(self):
        '''数据的初始化，用户信息保存格式为用户名：【密码，登录时间(time())用于计算)
        登录时间(ctime(),用于显示)】'''
        self.db = {}
        self._superName = 'fzyz.abc'
        self._superpasswd = 'fzyz'

    def userLogin(self, name, passwd):
        '''用户的登录，支持新用户和老用户的一起登录，不区分大小写的用户名，新用户自动注册'''
        try:
            if self.db[name.lower()][0] == passwd:
                if time.time() - self.db[name.lower()][1] < 14400:     #登录时间小于4小时
                    contents.SetValue('you already logged in at:' + str(self.db[name.lower()][2]))
                else:
                    contents.SetValue('Welcome back!')
        except IndexError:
            for i in name.lower():
                if i in string.punctuation + string.whitespace:
                    contents.SetValue('用户名不允许符号和空格符，请重新输入')
                    return False
            self.db[name.lower()] = [passwd, time.time(), time.ctime()]
        return True

    def delUser(self, name):
        '''通过超级用户进行用户的删除'''
        if userName == self._superName and userPw == self._superpasswd:
            del self.db[name.lower()]
        else:
            contents.SetValue('超级用户账户或密码输入有误')
            return

    def showAllUser(self):
        '''通过超级用户，显示所有的用户'''
        if userName == self._superName and userPw == self._superpasswd:
            for key in self.db.keys():
                contents.AppendText('用户名： %s', key)
        else:
            contents.SetValue('超级用户账户或密码输入有误')

def load(event):
    oneUser = UserPw()
    oneUser.userLogin(str(userName), str(userPw))

def delUser(event):
    oneUser = UserPw()
    oneUser.delUser(str(name))

def showAllUser(event):
    oneUser = UserPw()
    oneUser.showAllUser()

if __name__ == "__main__":
    app = wx.App()
    win = wx.Frame(None, title = '登录系统', size = (410, 335))
    userName = wx.TextCtrl(win, pos = (5, 5), size = (240, 25))
    userPw = wx.TextCtrl(win, pos = (5, 30), size = (240, 25))

    contents = wx.TextCtrl(win, pos = (5, 90), size = (390, 260),style = wx.TE_MULTILINE | wx.HSCROLL)

    loadButton = wx.Button(win, label = '登录', pos = (250, 5), size = (80, 25))
    loadButton.Bind(wx.EVT_BUTTON, load)

    delUserButton = wx.Button(win, label = '删除用户', pos = (5, 60), size = (90, 25))
    delUserButton.Bind(wx.EVT_BUTTON, delUser)

    showAllUserButton = wx.Button(win, label = '显示所有用户', pos = (100, 60), size = (110, 25))
    showAllUserButton.Bind(wx.EVT_BUTTON, showAllUser)

    win.Show()
    app.MainLoop()