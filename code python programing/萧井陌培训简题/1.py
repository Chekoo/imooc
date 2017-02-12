#coding=utf-8
# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10


from string import letters, digits
nums = digits
letter_num = letters + nums

def va():
    str = raw_input('Enter a string: ')
    if 2 <= len(str) <= 10:
        if str[0] not in letters or str[-1] not in letter_num:
            return False
        else:
            for i in str[1:]:
                if i not in (letter_num + '_'):
                    return False
            else:
                return True

if __name__ == "__main__":
        print va()
