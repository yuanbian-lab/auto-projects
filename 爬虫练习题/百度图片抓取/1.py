# -*- coding=utf-8 -*-
import requests
import re


url = "某度的图片搜索结果页"
url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE%CD%BC%C6%AC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDEsMiw2LDQsNSw3LDgsOQ%3D%3D"

response = requests.get(url)
imgs = re.findall("<img", response.text)
print(imgs)

