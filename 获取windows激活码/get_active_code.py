# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_kms_keys():
    url = "https://learn.microsoft.com/zh-cn/windows-server/get-started/kms-client-activation-keys"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("请求失败:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    keys = []

    # 遍历所有表格行，提取密钥
    for row in soup.select("table tr")[1:]:
        cols = row.find_all("td")
        if len(cols) >= 2:
            edition = cols[0].text.strip().encode('latin1').decode('utf8')
            key = cols[1].text.strip()
            # keys.append((edition, key))
            yield edition, key

