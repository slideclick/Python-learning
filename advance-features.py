


L =[]
n = 1
while n<=99:
	L.append(n)
	n = n +2

#切边- slice
L = ["A","B","C"]
L[0:3] #not include 3
L[-2:]


L = range(100)
L[:10]
L[-10:]
L[10:20]

L[:10:2] #every 2 elements in first 10 elements
L[::5] #every 5 elements
L[:] #copy a list


(0,1,2,3,4,5)[:3]

#string can also take slice
'ABCDEFG'[:3]

#迭代，iteration
d = {"a":1,"b":2,"c":3}
for key in d:
	print key

#for value in d.itervalues()
#for value in d.iteritems()

#check whether a object is iterable
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代True
isinstance(123, Iterable)

#use enumerate() function to realize index iteration
for i,value in enumerate(["A","B","C"]):
	print i, value

for x, y in [(1,1),(2,4),(3,9)]:
	print x,y 

#list comprehensions
#create list easily
L = []
for x in range(1,11): #from 1 to 10
	L.append(x*x)

L

[x*x for x in range(1,11)]
[x * x for x in range(1, 11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'XYZ'] #double iteration


import os
[d for d in os.listdir(".")] #os.listdir可以列出文件和目录


#iterate 2 variables simontenously
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
	print k, "=", v

#use tew variable to make list
[k+" = "+v for k,v in d.iteritems() ]


L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]


L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() if isinstance(s,str) else s for s in L]


#generator 生成器

g = (x * x for x in range(10))
g  #generator objecr
g.next() #g store the algorithm, each time call g.next(), return next element

# generator object is iterable
#usually use iteration to get its elements
g = (x * x for x in range(10))
for n in g:
	print n

#use generator to make complex elements
#first consider a function
def fab(max):
	n, a,b = 0, 0 ,1
	while n<max:
		print b
		a, b = b,a+b
		n = n+1

fab(6)

# a generator
def fab(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n = n+1

fab(6)

for n in fab(6):
	print n














