#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
	pass

s = Student();
s.name = "Michael" #dynamically add a class membet
print s.name

# bound a method to a instance
def set_age(self,age):
	self.age = age
	
from types import MethodType
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
print s.age

# not work in another instance in same class
s2 = Student()
# s2.set_age(25)

# bound a method to a class
def set_score(self,score):
	self.score = score

Student.set_score = MethodType(set_score,None,Student)
s.set_score(100)
print s.score
s2.set_score(99)
print s2.score


# to limit members of a class -> use _slots_
class Student(object):
	__slot__ = ('name','age')  #name of members allowed to be bounded

s = Student()
s.name = "Michael"
s.age = 25
# s.score = 99 # failed

# __ slot__ not work for subclass, only if __slot__ is also defined in subclass
# need further clarification
class GraduateStudent(Student):
	pass

g = GraduateStudent()
g.score = 9999
print g.score








