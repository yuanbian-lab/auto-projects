# -*- coding=utf-8 -*-
import requests

url = "https://blog.csdn.net/qq409732112/article/details/120896512"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

html_data = response.text

from lxml import html

dom = html.document_fromstring(html_data)
# 找到的节点id是article_content
# 使用样式选择器选择
el = dom.cssselect("#article_content")
content = el[0].text_content()
# 写入文件 - 文件只包含我们要的数据部分
with open("blog.txt", "w", encoding="utf-8") as f:
    f.write(content)