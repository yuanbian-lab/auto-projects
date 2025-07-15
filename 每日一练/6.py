# -*- coding=utf-8 -*-

def list2dict(input_list):
    my_dict = dict(input_list)
    return my_dict


# 函数调用示例
tuple_list = [(1, 'apple'), (2, 'banana')]
my_dict = list2dict(tuple_list)
print(my_dict)
