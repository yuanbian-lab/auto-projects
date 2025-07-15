# -*- coding=utf-8 -*-
number_list = [3, 5, 2, 4, 1, 6]
max_num = number_list[0]
for number in number_list[1:]:
    if max_num < number:
        max_num = number
print("列表中最大项是", number)