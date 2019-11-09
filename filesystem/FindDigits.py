#!/usr/bin/env python3

import os
import sys

def finddigits(path):
	res = ""
	with open(path) as file:
		try:
			while True:
				text_line = file.readline()
				if text_line:
					print(type(text_line), text_line)
					for char in text_line:
						if char.isdigit():
							res += char
				else:
					break
		finally:
			file.close()
	print(res)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		finddigits(sys.argv[1])
	else:
		sys.exit(-1)
	sys.exit(0)
