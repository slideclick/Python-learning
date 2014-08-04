#!/usr/bin/env python
# -*- coding: utf-8 -*-
#OOP



# class: key word to define a class
# Student: class name
# object: where it inherits

#a student class instance
bart  = Student()
bart
Student

#绑定属性
bart.name = "Bart Simpson"
bart.name

class Student(object):
	def __init__(self, name,score):#self point to the instance itself
		self.name = name
		self.score = score

	def print_score(self):
		print "%s: %s" %(self.name, self.score)



bart.name

#method just same as function- but its first argument is self

#encapsulation

#访问限制
class Student(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score  #can not be accessed outside the class

	def print_score(self):
		print "%s: %s" % (self.__name,self.__score)


#inheritance & polymorphism

class Animal(object):
	def run(self):
		print "Animal is running"

class Dog(Animal):
	pass

class Cat(Animal):
	pass

#subclass can get all method of superclass
dog = Dog()
cat = Cat()
dog.run()

#add some mthods to subclass
class Dog(Animal):
	def run(self):
		print "Dog is running..."
	def eat(self):
		print "Eating meat..."

dog = Dog()
dog.run()

#判断数据类型- 多态
isinstance(dog,Animal)
isinstance(dog,Dog)

#多态的应用
def run_twice(animal):
	animal.run()

run_twice(Dog())
run_twice(Cat())
run_twice(Animal())


#这就是著名的“开闭”原则：
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

#继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
#子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；

#===========
#获取对象信息

#type()- return type 类型
type(123)
type('str')
type(None)

type(abs)

#compare type
#simple way

type(123) == type(456)
type(123) == type('str')

import types
type("abc") == types.StringType
type(u"abx") == types.UnicodeType
type([]) == types.ListType
type(int)==type(str)==types.TypeType

#isinstance() to identify class type
a = Animal()
d = Dog()
c = Cat()

isinstance(d,Dog)
isinstance(d,Animal)

isinstance('a', (str, unicode))
isinstance(u'a', basestring)


#dir()= 获得一个对象的所有属性和方法
dir("ABC")

#equivelent
len('ABC')
'ABC'.__len__()

#自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyObject(object):
	def __len__(self):
		return 1000

obj = MyObject()
len(obj)

#普通属性 方法
"ABC".lower()

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()
#我们可以直接操作一个对象的状态：

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()
#test this object's attributes
hasattr(obj,"x") #有属性'x'吗？
hasattr(obj, 'y') # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') # 有属性'y'吗？
getattr(obj, 'y') # 获取属性'y'
obj.y

#试图获取不存在的属性，会抛出AttributeError的错误
getattr(obj,"z")
#传入一个default参数，如果属性不存在，就返回默认值：
getattr(obj,"z",404)

#也可以获得对象的方法：
hasattr(obj,"power")
getattr(obj,"power")
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn
fn() #same as obj.power()


#希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
def readImage(fp): #pass in an object want to read
	if hasattr(fp,"read"):
		return readData(fp)
	return None

























