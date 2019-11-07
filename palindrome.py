#!/usr/bin/env python3
print("""\
... def 函数名(参数):
... 	语句1
...		语句2
... """)
def palindrome(s):
	return s == s[::-1]

if __name__ == '__main__':
	s = input("Please enter a string: ")
	if palindrome(s):
		print("The string is a palindrome")
	else:
		print("The sting is not a palindrome")
