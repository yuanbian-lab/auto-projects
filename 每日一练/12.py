# -*- coding=utf-8 -*-
def is_palindrome(s):
    # 去除字符串中的空格并转换为小写
    s = s.replace(' ', '').lower()
    # 判断字符串是否等于其反转后的字符串
    return s == s[::-1]

# 接受用户输入的字符串
user_input = input("请输入一个字符串：")
# 调用函数判断字符串是否是回文字符串
if is_palindrome(user_input):
    print("该字符串是回文字符串")
else:
    print("该字符串不是回文字符串")