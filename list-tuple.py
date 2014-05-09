#!/usr/bin/env python
# -*- coding: utf-8 -*-


#list
classmate = ["A","b","C"]
classmate
len(classmate) #get number of elements in a list
#inde the list, start from 0
classmate[0]
classmate[1]
classmate[3] #out of range
#use -1 to get last element
classmate[-1]
classmate[-2]
classmate[-4] #out of range again

#append element to the end of list
classmate.append("Adam")
classmate
#append elements to specific position on a list
classmate.insert(1, 'Jack') #notics: start with 0
classmate

#delete the last element in a list- pop()
classmate.pop()
classmate
#delete a specific element
classmate.pop(1)
classmate

#replace element
classmate[1] = "Sarah"
classmate

#list can strore various data type
L = ['Apple', 123, True]
L
s = ['python', 'java', ['asp', 'php'], 'scheme']
len(s)

s[2][1]


#empty list
L = []
L
len(L)


#tuple
#similar to list, but immutable
t = ()
t = (1)
t = (1,)
t = ('a', 'b', ['A', 'B'])
t
t[2][0] = 'X'
t[2][1] = 'Y'
t








