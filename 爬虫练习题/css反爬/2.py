# -*- coding=utf-8 -*-
# 创建字体映射表
mapping_table = str.maketrans("这是一道非常鲜美的菜", "那是一棵挺拔高耸的树")

# 给正常人看的信息
origin_info = "这是一道菜"

# 爬虫实际抓取的
spider_info = origin_info.translate(mapping_table)
print(spider_info)