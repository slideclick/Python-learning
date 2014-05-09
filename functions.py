
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError("bad operand type")
	if x>=0:
		return x
	else:
		return -x

#function return multiple values
import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny #actually return a tuple

r = move(100,100,3,math.pi/6)


#必选参数， 默认参数，可变参数，关键字参数


def power(x, n = 2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s


#默认参数的问题
def add_end( L = []):
	L.append("END")
	return L

add_end()
add_end()
add_end()

#默认参数需指向不变对象！
def add_end(L = None):
	if L is None:
		L = []
	L.append("END")
	return L

add_end()
add_end()

#可变参数

#first consider use List of tuple
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum

cals([1,2,3,4])

# *number接受可变蚕食
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum

calc(1,2,3,4)
calc()
number = [1,2,3]
calc(*number)

#关键字参数: 它可以扩展函数的功能,如果调用者愿意提供更多的参数，我们也能收到
#关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):    
	print 'name:', name, 'age:', age, 'other:', kw

#只传必选参数
person("Michael",30)
#传入任意个数的关键字参数
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

#也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw) ##注意 **

#参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):    
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1,2)
func(1,2,c=3)
func(1,2,3,"a","b")
func(1,2,3,'a','b',x=99)

args = (1, 2, 3, 4,4,5,6)
kw = {'x': 99}
func(*args, **kw)


#recusrion function
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

fact(1000) #maximum recursion depth exceeded

#incorporate tail recusion
def fact(n):    
	return fact_iter(1, 1, n)

def fact_iter(product, count, max):    
	if count > max:        
		return product    
	return fact_iter(product * count, count + 1, max)






