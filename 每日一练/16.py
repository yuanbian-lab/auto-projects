# -*- coding=utf-8 -*-
def longest_word(sentence):
    # 拆分单词
    words = sentence.split()
    # 用字典存储结果， 长度为key，单词为键值
    longest_words = {}

    # 遍历单词列表
    for word in words:
        # 计算长度
        length = len(word)
        # 添加到字典
        longest_words[length] = word
    # 通过max函数获得最长的key
    print(longest_words)
    max_key = max(longest_words)
    # 返回最长单词列表
    return longest_words[max_key]

sentence = input("请输入一条语句：")
result = longest_word(sentence)
print("最长的一个单词是:", result)