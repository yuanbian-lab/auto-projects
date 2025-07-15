# -*- coding=utf-8 -*-
import math

def calculate_min_buckets(r, h):
    volume_per_bucket = math.pi * (r**2) * h
    min_buckets = math.ceil(15*1000 / volume_per_bucket)
    return min_buckets


r, h = input("请输入圆桶的半径与深度：").split()
r = float(r)
h = float(h)
result = calculate_min_buckets(r, h)
print(f"牛至少需要喝 {result} 桶水才能解渴。")