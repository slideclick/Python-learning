#!/usr/bin/env python
# -*- coding: utf-8 -*-


#unicode - UTF-8


#ASCII
ord("A")
chr(65)

print u"香港中文大学"
u"香港中文大学"
"香港中文大学"
print u'\u9999\u6e2f\u4e2d\u6587\u5927\u5b66' #print chinese
print '\u9999\u6e2f\u4e2d\u6587\u5927\u5b66'

#transform Unicode to UTF-8
u'ABC'.encode('utf-8')
u'中文'.encode('utf-8')

#alphbets are same for Unicode and UTf-8
len(u'ABC') #3
len('ABC') #2

len(u'中文')
len('\xe4\xb8\xad\xe6\x96\x87')

#tranfrom utf-8 to unicode
'abc'.decode('utf-8') #u'abc'
'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') #u'\u4e2d\u6587'
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#格式化输出
'Hello, %s' % 'world'
'Hi, %s, you have $%d.' % ('Michael', 1000000)

'%2d-%02d' % (3, 1) #补零
'%.2f' % 3.1415926 #小数位数

# %s is most useful...

#转义字符- %% -> %
'growth rate: %d %%' % 7






