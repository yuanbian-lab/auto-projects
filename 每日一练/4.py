# -*- coding=utf-8 -*-
import re
while True:
    sentences = input("请输入一条英文语句:")
    if sentences == "quit":
        break
    # 英文句子中单词间用空格隔开
    # 本题要求其他符号也进行分割
    # 使用正则分割句子
    words_list = re.split("\W", sentences.lower())
    count = {}
    for word in words_list:
        count[word] = count.get(word, 0) + 1
    # 获得出现次数最大值
    max_number = max(count.values())
    # 输出出现次数最大项
    print([key for key, val in count.items() if val == max_number])

