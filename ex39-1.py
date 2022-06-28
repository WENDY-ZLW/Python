#This python file uses the following encoding: utf-8
#带顺序的字典，普通的字典每次打印出的顺序不统一
import collections

print("\nOrder dictionary")
d = collections.OrderedDict()
d['a']='A'
d['b']='B'
d['c']='C'
d['2']='2'
d['1']='1'

for k,v in d.items():
    print [k,v]
    
