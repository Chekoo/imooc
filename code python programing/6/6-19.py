#coding=utf-8
def print_table(container, column_count=1, row_sort=True):
    """按照指定列数输出一个可遍历容器
    container:容器
    column_count: 列数
    row_sort:{True:行排序 | False:列排序}"""
    lens = len(container)                    #容器长度
    row_count = lens // column_count         #全部填满的行数
    tail = lens % column_count               #最后留下的小尾巴的数量
    spaces = column_count - tail             #最后一行的空位数量

    if row_sort:
        for i in range(lens - tail):         #先把满的行输出
            print "%10d" %container[i],
            if i % column_count == column_count - 1:
                print '\n',
        for i in range(spaces):              #输出最后一行的空格
            print "%10s" % "",
        for i in range(lens - tail, lens):  #输出最后一行剩下的数
            print '%10d' % container[i],
        print '\n',

    else:
        strings = ['' for r in range(row_count + 1)]     #定义一个列表存储每行的输出
        i = 0
        r = 0
        # 本算法顺次遍历每一列，然后判断如果为最后一行并且还有没输出的空格


        spaces = column_count - tail            #存储最后一行的空格数
        while i < lens:                         #遍历每一个元素
            if r == row_count and spaces:       #如果是最后一行且还有没输出的空格
                strings[r] += '%10s' % ''
                spaces -= 1
            else:
                strings[r] += '%10d' %container[i]
                i += 1
            r += 1
            if r == row_count + 1:
                r = 0
        print '\n'.join(strings)


if __name__ == '__main__':
    print_table(range(103), 3, True)

