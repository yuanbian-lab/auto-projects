# -*- coding=utf-8 -*-
import re

def longest_word(sentence):
    # 移除标点符号
    sentence = re.sub(r'[^\w\s]', '', sentence)
    # 拆分单词
    words = sentence.split()
    # 初始化最长单词列表
    longest_words = []
    # 初始化最大长度
    max_length = 0
    # 遍历单词列表
    for word in words:
        # 计算长度
        length = len(word)
        # 如果长度超过最大长度，则更新最大长度和最长单词列表
        if length > max_length:
            max_length = length
            longest_words = [word]
        # 如果长度等于最大长度，则将单词添加到最长单词列表中
        elif length == max_length:
            longest_words.append(word)
    # 返回最长单词列表
    return longest_words