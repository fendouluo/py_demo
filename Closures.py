#!/usr/bin/env python3
'''
闭包（Closures）是由另外一个函数返回的函数。我们使用闭包去除重复代码
'''
def add_number(num):
	def adder(number):
		return num + number
	return adder
a_10 = add_number(10)
print(a_10(21))
print(a_10(34))

