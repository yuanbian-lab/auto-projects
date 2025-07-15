# -*- coding=utf-8 -*-

# 永久循环， 用户输入0退出
while True:
    year = int(input("请输入一个年份: "))
    if not year:
        print("感谢您使用闰年计算器")
        break

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "是闰年")
    else:
        print(year, "不是闰年")
