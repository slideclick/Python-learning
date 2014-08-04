#!/usr/bin/env python
# -*- coding: utf-8 -*-

#读文件
f = open('test.txt','r')
f.read()
f.close()

#为了保证无论是否出错都能正确地关闭文件，
#我们可以使用try ... finally

try:
	f = open('path/to/file','r')
	print f.read()
finally:
	if f:
		f.close()

with open('test.txt','r') as f:
	 print f.read()

#写文件
f = open('test.txt','w')
f.write("Hello, World!")
f.close 
#操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
#空闲的时候再慢慢写入。只有调用close()方法时，
#操作系统才保证把没有写入的数据全部写入磁盘

