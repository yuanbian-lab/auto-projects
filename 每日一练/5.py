# -*- coding=utf-8 -*-
def flip_dict(_input_dict):
    _output_dict = {val: key for key, val in _input_dict.items()}
    return _output_dict


# 函数调用示例
input_dict = {"A": 1, "B": 2, "C": 3}
output_dict = flip_dict(input_dict)
print(output_dict)
