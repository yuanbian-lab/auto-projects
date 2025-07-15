# -*- coding=utf-8 -*-
"""已录"""
def myfun(arg1, arg2):
    arg1.append(arg2)
a = []
myfun(a, 1)
myfun(a, 2)
myfun(a, 3)
print(a)