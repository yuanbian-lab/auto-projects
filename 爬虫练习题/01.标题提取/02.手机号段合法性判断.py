# -*- coding=utf-8 -*-
"""
判断手机号的合法性
"""
# 如果有其他允许的号段可以加入
# mobile_prefix = ("189", "139", "158")
#
# while True:
#     mobile = input("请输入手机号:")
#     if not mobile:
#         break
#     # 判断长度、 判断前缀、判断是否数字组成
#     if len(mobile) != 11 \
#             or mobile[:3] not in mobile_prefix\
#             or not mobile.isdigit() :
#         print("您输入的手机号不正确")
#     else:
#         print("您输入的手机号可以使用")

# 使用正则
# 正则如何检测是数字组成
# \d代表数字，{11}表示需要11个
rule = "\d{11}"
# 如何检测前缀
# ^表示开头 $表示末尾
rule = "^189\d{8}$"
# 再加上几个号段
rule = "^(189|139|158)\d{8}$"

import re

while True:
    mobile = input("请输入手机号:")
    if not mobile:
        break
    if re.match(rule, mobile):
        print("您输入的手机号可以使用")
    else:
        print("您输入的手机号不可以使用")