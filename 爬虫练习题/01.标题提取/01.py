# -*- coding=utf-8 -*-
# 网页源码片段
html_string = """
<a href="yuanbian-lab">猿变AI实验室</a>
<a href="pythonp-xp">老六工作室</a>
"""
# 提取规则
# 需要的数据都在href=" .... "中
# 写下
rule = 'href="数据部分"'
# 数据部分是有英文字母与-符号组成
# 英文字母可以使用[a-z]， 也可以使用\w表示
# 所以规则是 [\w-]+, +表示由多个字母组成
# rule = 'href="([\w-]+)"'
rule = 'href="(.*)"'
# 导入正则模块
import re

data = re.findall(rule, html_string)
print(data)