#!/usr/bin/env python
# -*- coding: utf-8 -*-

#try...except...finally

#try
#用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
#而是直接跳转至错误处理代码，即except语句块，执行完except后，
#如果有finally语句块，则执行finally语句块，至此，执行完毕。

try:
	print "try..."
	r = 10/0
	print "result:",r
except ZeroDivisionError, e:
	print "except", e
finally:
	print "finally...."

#try...
#except integer division or modulo by zero
#finally....

try:
	print "try..."
	r = 10/2
	print "result:",r
except ZeroDivisionError, e:
	print "except", e
finally:
	print "finally...."

#try...
#result: 5
#finally....

#有多个except来捕获不同类型的错误：
try:
	print "try..."
	r = 10/int('a') #on error here
	print 'result:', r
except ValueError, e:
	print "ValueError",e
except ZeroDivisionError,e:
	print "ZeroDivisionError:",e
finally:
	print "finally"

#如果没有错误发生，可以在except语句块后面加一个else，
#当没有错误发生时，会自动执行else语句：
try:
	print "try..."
	r = 10.0/int(0.1) #on error here
	print 'result:', r
except ValueError, e:
	print "ValueError",e
except ZeroDivisionError,e:
	print "ZeroDivisionError:",e
else:
	print "no error!"
finally:
	print "finally"

#所有的错误类型都继承自BaseException
#不但捕获该类型的错误，还把其子类也“一网打尽”

try:
	foo()
except StandardError, e:
	print "StandardError",e
except ValueError,e: # can never be catched, since valueerror is subclass of standarderror
	print "ValueError",e


#可以跨越多层调用
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar('0')
	except StandardError,e:
		print "Error!",e
	finally:
		print 'finally...'


#调用堆栈
#如果错误没有被捕获，它就会一直往上抛
def foo(s):    
	return 10 / int(s)

def bar(s):    
	return foo(s) * 2

def main():    
	bar('0')

main()

#记录错误
#捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，
#同时，让程序继续执行下去
import logging
def foo(s):    
	return 10 / int(s)

def bar(s):    
	return foo(s) * 2

def main():    
	try:        
		bar('0')    
	except StandardError, e:        
		logging.exception(e)

main()
print 'END'

#抛出错误
#首先根据需要，可以定义一个错误的class，选择好继承关系，
#然后，用raise语句抛出一个错误的实例
class FooError(StandardError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError("invalid value: %s" % s)
	return 10/n

#raise语句如果不带参数，就会把当前错误原样抛出。此外，
#在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
	10/0
except ZeroDivisionError, e:
	raise

try:
	10/0
except ZeroDivisionError, e:
	raise ValueError("input error!")






