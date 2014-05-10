#!/usr/bin/env python
# -*- coding: utf-8 -*-

"a test module" #文档注释

__author__ = "Jared Zhou" #作者

import sys

def test():
	args = sys.argv
	if len(args) ==1:
		print "Hello, world!"
	elif len(args) == 2:
		print "Hello, %s!" % args[1]
	else:
		print "Too many arguements!"


if __name__ == "__main__": #for run module at terminal
	test()


try:
	import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError    
	import StringIO

