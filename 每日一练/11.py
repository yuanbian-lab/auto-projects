# -*- coding=utf-8 -*-
"""
请编写一段程序求他最大公约数
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

print("最大公约数为：", gcd(num1, num2))