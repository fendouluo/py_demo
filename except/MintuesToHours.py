#!/usr/bin/env python3

import sys
import os

def Hours(minute):
	if minute < 0:
		raise ValueError("Input number cannot be negative")
	else:
		print("{} H {} M".format(int(minute / 60), int( minute % 60)))

if __name__ == "__main__":
	if len(sys.argv) > 1:
		try:
			Hours(int(sys.argv[1]))
		except:
			print("Parameter Error")
	else:
		sys.exit(-1)
	sys.exit(0)
