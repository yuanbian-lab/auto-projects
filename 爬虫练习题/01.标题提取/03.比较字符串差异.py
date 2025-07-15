# -*- coding=utf-8 -*-
# 复杂的需要通过动态规划
# 比较两个字符串的差异
string_1 = "hellO worlD"
string_2 = "Hello World"
for index, char in enumerate(string_1):
    if string_2[index] != char:
        print(f"{string_2[index]} 替换了 {char} ")



for data in zip(string_1, string_2):
    if data[1] != data[0]:
        print(f"{data[1]} 替换了 {data[0]} ")