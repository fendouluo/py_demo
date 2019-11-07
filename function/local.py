#!/usr/bin/env python3
def change():
	a = 90
	print(a)

def change2():
	global a
	a = 90
	print(a)

a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)
print("Before the function2 call ", a)
print("inside change2 function", end=' ')
change2()
print("After the function2 call ", a)
