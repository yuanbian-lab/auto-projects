# -*- coding=utf-8 -*-
# 导入json模块
import json

string = """
{
    "name": "Alice",
    "age": 30,
    "is_student": false,
    "hobbies": ["reading", "hiking"]
}
"""
# 将string值转换为python对象
# result是一个字典
result = json.loads(string)
print(result['name'])
# result['hobbies']是一个列表
print(result['hobbies'][0])

data = [
    {"name": "老六", "age": 28, "single": False},
    {"name": "Carl", "age": 32, "house": None}
]

import json

string = json.dumps(data)
print(string)