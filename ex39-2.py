#This python file uses the following encoding: utf-8
#通过改变传入的顺序来判断是否是同一个dict
import collections
d2={}
d2['a'] = 'A'
d2['b'] = 'B'
d2['c'] = 'C'

d3={}
d3['c'] = 'C'
d3['a'] = 'A'
d3['b'] = 'B'
print(d2 == d3)  #True
print('\nOrderedDict:')

d4=collections.OrderedDict()
d4['a'] = 'A'
d4['b'] = 'B'
d4['c'] = 'C'

d5=collections.OrderedDict()
d5['c'] ='C'
d5['a'] ='A'
d5['b'] ='B'
print(d4 == d5)  #False

#如果是普通的字典，即使传入的顺序不一样，但是依然是相同的字典; d2d3
#如果是orderedDict,传入的顺序不一样，那么得到的字典是不一样的。d4d5