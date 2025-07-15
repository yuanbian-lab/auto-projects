# -*- coding=utf-8 -*-
from lxml import html
html_string = """
<table id="functions">
    <tr><td>函数名</td><td>使用方法</td><td>备注</td></tr>
    <tr><td>int</td><td>将其他类型转换为整数</td><td>输入必须是数字</td></tr>
    <tr><td>float</td><td>将其他类型转换为浮点数</td><td>输入必须是数字</td></tr>
    <tr><td>str</td><td>将其他类型转换为字符串</td><td>与repr有区别</td></tr>
</table>
"""
dom = html.document_fromstring(html_string)
table = dom.cssselect("#functions")
tr_list = table[0].findall("tr")
tr_data_list = []
for tr in tr_list:
    td_text_list = tr.xpath(".//td/text()")
    tr_data_list.append(td_text_list)
print(tr_data_list)


with open("table_data.txt", "w") as f:
    # 一行表格数据存为文件的一行
    for tr_data in tr_data_list:
        # 使用逗号拼接td单元数据为一行
        line = ",".join(tr_data)
        f.write(line+"\n")