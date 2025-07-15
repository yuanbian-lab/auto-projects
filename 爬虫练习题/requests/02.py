# -*- coding=utf-8 -*-
import requests


url = "爬取网址" # GET参数从URL中获得

# 设置headers
# headers是一个字典
# 请求头参数名：请求参数值
headers = {
    "Accept": "image/png",
    "User-Agent": "Yuanbian Spider",
    "Cookie": "username=老六" # 通常的cookie会加密
}
# 在GET方法中添加headers关键字参数
response = requests.get(url, headers=headers)

# 对于cookie， 还可以单独设置
# 关于cookie， 后续笔记详细介绍
cookies = {}
response = requests.get(url, headers=headers, cookies=cookies)