# -*- coding=utf-8 -*-
import requests

url = "https://book.douban.com/"
# 设置请求头 User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                  " AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
# response = requests.get(url, headers=headers)
# html_string = response.text
# print(response.status_code)
with open("test.html", "r") as f:
    html_string = f.read()

from lxml import html

dom = html.fromstring(html_string)
containers = dom.cssselect(".slide-list")
div_container = containers[0]


books_info = div_container.cssselect(".info")
print(books_info)
books = []
for book_info in books_info:
    title_div = book_info.cssselect(".title")[0]
    author_div = book_info.cssselect(".author")[0]
    # 放入列表中
    title = title_div.text_content()
    author = author_div.text_content()
    books.append((title, author))
print(books)


with open("books.csv", "w") as f:
    for book in books:
        # 去多余空格、换行符
        title = book[0].strip()
        author = book[1].strip()
        # 向文件中写入一行数据
        f.write(f"{title}, {author}\n")
