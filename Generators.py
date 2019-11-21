#!/usr/bin/env python3
from collections import Iterator

def my_generator():
	print("Inside my generator")
	yield 'a'
	yield 'b'
	yield 'c'

for char in my_generator():
	print(char)

def counter_generator(low, high):
	while low <= high:
		yield low
		low += 1

for i in counter_generator(1,20):
	print(i, end=' ')

def infinite_generator(start=0):
	while True:
		yield start
		start += 1

for num in infinite_generator(10):
	print(num, end=' ')
	if num > 20:
		break
print()

class Counter(object):
	def __init__(self, low, high):
		self.low = low
		self.high = high
	def __iter__(self):
		counter = self.low
		while self.high >= counter:
			yield counter
			counter += 1

gobj = Counter(5,10)
for num in gobj:
	print(num, end=' ')
print()

class Test():
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __iter__(self):
		return self
	def __next__(self):
		self.a += 1
		if self.a > self.b:
			raise StopIterarion()
		return self.a

test = Test(1, 10)
print(isinstance(test, Iterator))

'''
表达式（Generator expressions），生成器表达式是列表推导式和生成器的一个高性能，内存使用效率高的推广。

举个例子，我们尝试对 1 到 9 的所有数字进行平方求和。

>>> sum([x*x for x in range(1,10)])
这个例子实际上首先在内存中创建了一个平方数值的列表，然后遍历这个列表，最终求和后释放内存。你能理解一个大列表的内存占用情况是怎样的。

我们可以通过使用生成器表达式来节省内存使用。

>>> sum(x*x for x in range(1,10))
'''

jobtext = 'anacron'
all = (line for line in open('/etc/crontab', 'r'))
jobj = (line for line in all if line.find(jobtext) != -1)
for line in jobj:
	print(line, end=' ')
print()


