# -*- coding=utf-8 -*-


while True:
    num = int(input("请输入一个正整数："))
    # 初始化阶乘结果为1
    factorial = 1
    if num < 0:
        print("输入的数必须是正整数！")
    elif num == 0:
        print("0的阶乘为1")
    else:
        # 计算阶乘
        for i in range(1, num + 1):
            factorial *= i
        print(f"{num}的阶乘为：{factorial}")