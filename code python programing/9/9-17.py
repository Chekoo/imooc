#coding=utf-8
class fielEdit(object):
    def newFile(self, fileName, fileText):     #新建一个文件
        with open(fileName, 'a+') as fobj:
            fobj.write(fileText)

    def showFile(self, fileName):           #展示文件内容
        strTemp = ''
        with open(fileName) as fobj:
            for i in fobj:
                strTemp += i
        return strTemp

    def editFile(self, fileName, lineNum, newText):         #编辑文件内容
        lines = []
        with open(fileName) as fobj:
            lines = fobj.readlines()
            if lineNum > len(lines):                   #如果输入的行数大于文件行数
                return False
            lines[lineNum - 1] = newText               
        with open(fileName, 'w') as fobj:
            fobj.writelines(lines)

if __name__ == '__main__':
    while True:
        fobj = fielEdit()
        print 'n to newfile'
        print 's to showfile'
        print 'e to editfile'
        print 'q to quit file'
        choice = raw_input('please enter the choice: ')
        if choice.lower() == 'q':
            break
        if choice.lower() not in ['n', 's', 'e']:
            continue
        else:
            if choice.lower() == 'n':
                fileName = raw_input('please enter the filename: ')
                fileText = ''
                while True:
                    Text = raw_input('please enter the text(q to quit): ')
                    if Text.lower() == 'q':
                        break
                    fileText += Text
                    fileText += '\n'
                fobj.newFile(fileName, fileText)
            elif choice.lower() == 's':
                fileName = raw_input('please enter the filename: ')
                print fobj.showFile(fileName)
            elif choice.lower() == 'e':
                fileName = raw_input('please enter the filename: ')
                lineNum = int(raw_input('please enter the linenumber: '))
                lineText = raw_input('please enter the newText: ')
                fobj.editFile(fileName, lineNum, lineText)