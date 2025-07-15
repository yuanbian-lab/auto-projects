# -*- coding=utf-8 -*-
from datetime import datetime

# 从用户输入获取日期
date_string = input("请输入日期（格式为年/月/日）：")

try:
    # 将日期字符串转换为datetime对象
    date = datetime.strptime(date_string, "%Y/%m/%d")

    # 获取该日期是当年的第几天
    day_of_year = date.timetuple().tm_yday

    print("该日期是该年的第{}天".format(day_of_year))

except ValueError:
    print("输入的日期格式不正确")