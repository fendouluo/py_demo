#!/usr/bin/env python3

def high(l):
	return [i.upper() for i in l]
def test(h, l):
	return h(l)

l = ['python', 'Linux', 'Git']
print(list(test(high, l)))

lst = [1, 2, 3, 4, 5]
def square(num):
	#"返回所给数字的平方."
	return num * num

print(list(map(square, lst)))
