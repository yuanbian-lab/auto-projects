# -*- coding=utf-8 -*-
import requests
action_url = "https://www.douban.com/search"
# action_url = "https://www.douban.com/search?q=%E7%BA%A2%E6%A5%BC%E6%A2%A6"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                  " AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
# 传送的数据，与表单一致的键值对
data = {"q": "红楼梦"}
response = requests.get(action_url, params=data, headers=headers)

# 保存搜索结果，方便分析
with open("test.html", "w") as f:
    f.write(response.text)