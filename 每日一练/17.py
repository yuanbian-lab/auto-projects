# -*- coding=utf-8 -*-
def decorator(cls):
    class WrappedClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # 添加额外的初始化逻辑

        def some_additional_method(self):
            print("hello world")

    return WrappedClass

@decorator
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        print(f"Value: {self.value}")

# 使用装饰器修饰后的类
obj = MyClass(10)
obj.my_method()
obj.some_additional_method()