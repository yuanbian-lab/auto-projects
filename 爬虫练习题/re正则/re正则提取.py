# -*- coding=utf-8 -*-
# 网页源码片段
html_string = """<a href="/yuanbian_ai/playground?ai_type=2">猿变AI实验室</a>
"""
# 提取规则
# 需要的数据都在href=" .... "中
# .表示任意字符 *表示任意多个字符
rule = r'<a href="(.*)">(.*)</a>'
# 导入正则模块
import re
data = re.findall(rule, html_string)
print(data)

html_string = """<img src="/imgs/01.png" width="100" height="100" />
"""
rule = r'src="(.*?)"'
data = re.findall(rule, html_string)
print(data)


html_string = """<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
您的浏览器不支持Video标签。
</video>"""
rule = r'src="(.*)"'
data = re.findall(rule, html_string)
print(data)