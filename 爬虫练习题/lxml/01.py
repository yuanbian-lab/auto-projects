# -*- coding=utf-8 -*-
from lxml import etree
xml_data = """
<root>
  <data>数据1</data>
  <data>数据2</data>
  <data time="2050-10-1">数据3</data>
</root>
"""
# 使用 lxml 解析 XML 数据
root = etree.fromstring(xml_data)
data_list = root.findall("data")
for data in data_list:
    time = data.get("time")
    print(data.text, time)


books = """
<books>
    <book author="年轻的老六">爬虫入门</book>
    <book author="中年的老六">爬虫收入秘籍</book>
    <book author="懵逼的老六">爬虫通向何处</book>
</books>    
"""
root = etree.fromstring(books)
book_list = root.findall("book")
for book in book_list:
    author = book.get("author")
    name = book.text
    print(name, author)