#!/usr/bin/env python3
print("""\
... read() 方法一次性读取整个文件,read(size) 有一个可选的参数 size，用于指定字符串长度。如果没有指定 size 或者指定为负数，就会读取并返回整个文件。当文件大小为当前机器内存两倍时，就会产生问题。反之，会尽可能按比较大的 size 读取和返回数据
... readline() 能帮助你每次读取文件的一行
... readlines() 方法读取所有行到一个列表中
... fobj = open('sample.txt')
... for x in fobj:
...     print(x, end = '')
... 在实际情况中，我们应该尝试使用 with 语句处理文件对象，它会在文件用完后会自动关闭，就算发生异常也没关系。它是 try-finally 块的简写：
... with open('sample.txt') as fobj:
...     for line in fobj:
...         print(line, end = '')
... file = open('兼职模特联系方式.txt', 'r')  # 创建的这个文件，也是一个可迭代对象
try:
    text = file.read()  # 结果为str类型
    print(type(text))
    print(text)
finally:
    file.close()

file = open('兼职模特联系方式.txt', 'r')

try:
    while True:
        text_line = file.readline()
        if text_line:
            print(type(text_line), text_line)
        else:
            break
finally:
    file.close()

file = open('兼职模特联系方式.txt', 'r')

try:
    text_lines = file.readlines()
    print(type(text_lines), text_lines)
    for line in text_lines:
        print(type(line), line)
finally:
    file.close()

... """)
name = input("Enter the file name:")
fobj = open(name)
print(fobj.read())
fobj.close

