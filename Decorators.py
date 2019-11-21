#!/usr/bin/env python3
'''
装饰器（Decorators）用来给一些对象动态的添加一些新的行为，我们使用过的闭包也是这样的。
我们会创建一个简单的示例，将在函数执行前后打印一些语句。
'''
def my_decorator(func):
	def wrapper(*args, **kwargs):
		print("Before call")
		result = func(*args, **kwargs)
		print("After call")
		return result
	return wrapper

@my_decorator
def add(a, b):
	return a + b

print(add(1, 3))
