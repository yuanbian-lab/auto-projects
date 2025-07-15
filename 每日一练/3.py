# -*- coding=utf-8 -*-
# 定义一个学生列表
students_list = []
# 定义一个永久循环， 直到用户输入"quit"退出循环
while True:
    student_info = input("请输入学生信息:")
    if student_info == "quit":
        break
    # 将student_info由字符串分割成元组
    info = tuple(student_info.replace("，", ",").split(","))
    # 将信息添加到学生列表
    students_list.append(info)
# 使用推导式生成学生姓名名单
students_name = [info[2] for info in students_list]
print("包含的学生姓名数据：", students_name)
