#coding=utf-8
# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

def prime_num():
    list = [2, 3]
    for num in range(2, 101):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and num != i:
                break
            elif num % i != 0 and i == int(num ** 0.5):
                list.append(num)
    return list

if __name__ == '__main__':
    print prime_num()