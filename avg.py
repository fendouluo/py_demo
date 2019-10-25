#!/usr/bin/env python3
N = int(input("Enter your Digital number :"))

while N <= 0:
	N = int(input("Enter your Digital number :"))
a = 1
value = 0
avg = 0
while a <= N:
	tmp = float(input('Enter your the {} nuber: '.format(a)))
	value = value + tmp
	a = a + 1
avg = value / N
#print(avg)
print('N = {}, Sum = {}'.format(N, value))
print('avg is :{}'.format(avg))
	
