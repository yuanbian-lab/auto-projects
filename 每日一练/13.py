# -*- coding=utf-8 -*-
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间为 {end_time - start_time} 秒")
        return result
    return wrapper

@timer_decorator
def my_function():
    time.sleep(2)
    print("函数执行完毕")

my_function()