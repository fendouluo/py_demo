#!/usr/bin/env python3
print("""\
... read() 方法一次性读取整个文件,read(size) 有一个可选的参数 size，用于指定字符串长度。如果没有指定 size 或者指定为负数，就会读取并返回整个文件。当文件大小为当前机器内存两倍时，就会产生问题。反之，会尽可能按比较大的 size 读取和返回数据
... readline() 能帮助你每次读取文件的一行
... readlines() 方法读取所有行到一个列表中
... fobj = open('sample.txt')
... for x in fobj:
...     print(x, end = '')
... """)
name = input("Enter the file name:")
fobj = open(name)
print(fobj.read())
fobj.close

