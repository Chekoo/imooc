#coding=utf-8
def dollarize(fValue):
    strValue = str(fValue)
    isNegative = False
    if strValue[0] == '-':
        isNegative = True   #标记为True,后面将用到
        strValue = strValue[1:]    #去掉负号
    strMoney = strValue.split('.') #split返回分割后的列表
    #print 'strMoney', strMoney
    strTemp = []        #临时列表
    while (len(strMoney[0]) - 1) / 3: #进行分割，3位3位分开
        strTemp.append(strMoney[0][-3:])
        strMoney[0] = strMoney[0][:-3]
        #print 'strTemp', strTemp
        #print 'strMoney', strMoney
    strTemp.append(strMoney[0])
    strTemp.reverse()
    #print 'strTemp', strTemp
    myDoller = ','.join(strTemp) + '.' + strMoney[1]
    #print 'myDoller', myDoller
    if isNegative:
        myDoller = '-' + myDoller
    return myDoller

class MoneyFmt(object):
    def __init__(self, value = 0.0):
        self.value = dollarize(value)
    def update(self, value = None):
        self.value = dollarize(value)
    def __repr__(self):
        return repr(self.value)
    def __str__(self):
        val = '$'
        if self.value[0] == '-':
            val = '-$' + self.value[1:]
        else:
            val += self.value
        return val
    def __nonzero__(self):
        return bool(self.value)

if __name__ == "__main__":
    cash = MoneyFmt(1234567.8901)
    print cash
    acash = MoneyFmt(-123213.213123)
    print acash