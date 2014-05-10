#!/usr/bin/env python
# -*- coding: utf-8 -*-

#high-order function- function that can take functions as argument

#map()
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回

def f(x):
	return x * x

map(f,range(10))

#reduce()
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x,y):
	return x+y

reduce(add,range(10))

#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
	return x*10 +y

reduce(fn,[1,3,5,7,9])

#把str转换为int的函数：
def fn(x,y):
	return x * 10 + y

reduce(fn,map(int,"13579"))

def str2int(s):    #convert string to int
	def fn(x, y):        
		return x * 10 + y    
	return reduce(fn, map(int, s))

#use lambda function to further simplify
def str2int(s):    
	return reduce(lambda x,y: x*10+y, map(int, s))


#sorting
#core comcept: compare elements
sorted([36,5,12,9,21])

#sorted() is a high-order function
#it can take a compare function 

def reverse_cmp(x,y):
	if x>y:
		return -1
	if x<y:
		return 1
	else:
		return 0

sorted([36,5,12,9,21],reverse_cmp)

#string sorting
sorted(['about', 'bob', 'Zoo', 'Credit'])

#ignire upper case
def cmp_ignore_case(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1<u2:
		return -1
	if u1 > u2:
		return 1
	else:
		return 0

sorted(['about', 'bob', 'Zoo', 'Credit'],cmp_ignore_case)


#function as return value
#high-order function can also return function

#simple function to sum 
def cal_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

cal_sum(1,2,3,45)

#return fucntion for sum
#example of closure
def cal_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax +n
		return ax
	return sum

cal_sum(1,2,3,45)()
f1 = cal_sum(1,2,3,45)
f2 = cal_sum(1,2,3,45)
f1 == f2

#匿名函数 anonymous function
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])


#装饰器- decorator
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print "2014-5-10"

f = now
f()

#get function name
now.__name__
f.__name__

#代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator)
#本质上，decorator就是一个返回函数的高阶函数

def log(func): #pass in a function
#same as now = log(now)
	def wrapper(*args, **kw):
		print "call %s(): " % func.__name__
		return func(*args, **kw)
	return wrapper

@log #put decorator before the definition of the function 
def now():
	print "2014-5-10"

now()


#自定义log的文本
def log(text):
	def decorator(func):
		def wrapper(*args, ** kw):
			print "%s %s(): " %(text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

@log("execute") # same as now = log('execute')(now)
def now():
	print "2014-5-10"

now()

#above decoratot has problem
#now.__name__  is "wrapper"

import functools

def log(func): #pass in a function
#same as now = log(now)
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print "call %s(): " % func.__name__
		return func(*args, **kw)
	
	return wrapper

@log #put decorator before the definition of the function 
def now():
	print "2014-5-10"

now()

#===========================================#
#partial function 偏函数
int("12344")
int("1234",base = 8)

def int2(x , base = 2):
	return int(x,base)

int2('10000')
int2('1010101')

#use functools.patial() to create partial function
#把一个函数的某些参数（不管有没有默认值）给固定住（也就是设置默认值），返回一个新的函数
import functools
int2 = functools.partial(int, base = 2) #int2 is a functools.partial object
int2("100000")
int2("10000",base = 10)

















