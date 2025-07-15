# -*- coding=utf-8 -*-
# 定义一个单词列表
word_list = []

# 定义一个永久循环， 直到用户输入"quit"退出循环
while True:
    word = input("请输入单词:")
    if word == "quit":
        break
    if word in word_list:
        print(f"您输入的单词:{word}已经存在")
    else:
        word_list.append(word)
print("您输入的单词列表：", word_list)