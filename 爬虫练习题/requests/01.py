# -*- coding=utf-8 -*-
# 导入模块
import requests

# 发送 HTTP GET 请求
# 就好像我们在浏览器输入网址
# 什么是url请看No.2

response = requests.get('https://www.baidu.com')
print(response.cookies.values())

# response就是我们请求的网页数据
# 查看数据之前， 要检查是否请求成功
# 状态码是200才成功， 其他都是失败了，比如403， 404， 502
# 检查响应状态码
if response.status_code == 200:
    # 解析响应内容（假设响应内容是 JSON 格式）
    # 字节数据
    data = response.content
    # 根据网页编码解码数据
    data = data.decode("utf-8")
    # 处理响应数据
    print(data)
else:
    # 请求失败
    print('请求失败，错误码：', response.status_code)