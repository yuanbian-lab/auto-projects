# -*- coding=utf-8 -*-
import re
def longest_word(sentence):
    # 移除标点符号
    sentence = re.sub(r'[^\w\s]', '', sentence)
    # 拆分单词
    words = sentence.split()
    # 初始化最长单词列表
    longest_words = {}

    # 遍历单词列表
    for word in words:
        # 计算长度
        length = len(word)
        if longest_words.get(length):
            longest_words[length].append(word)
        else:
            longest_words[length] = [word]
    max_key = max(longest_words, key=longest_words.get)
    # 返回最长单词列表
    return longest_words[max_key]


sentence = "I love programming and Python is my favorite language."
result = longest_word(sentence)
print("Longest words:", result)
