# -*- coding=utf-8 -*-
html_string = """
<div>
    <p class="circle">段落1</p>
    <p>段落2
        <a href="链接url">链接</a>
    </p>
</div>
    """
from lxml import html

dom = html.fromstring(html_string)
# all_p = dom.find(".//p")
# # for p in all_p:
# print(all_p.text)
# all_p = dom.cssselect(".circle")
# print(all_p.text)
xpath = "//div/p[2]/text()"
text = dom.xpath(xpath)
print(text)