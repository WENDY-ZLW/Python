# This Python file uses the following encoding: utf-8
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # .split() 通过指定分隔符(' ')对字符串进行切片
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:  #不等于10即添加字符
    next_one = more_stuff.pop()#从more_stuff最后一个元素开始添加到stuff[]直至stuff中有10个元素
    print "Adding:", next_one
    stuff.append(next_one)#列表里的添加语句
    print "There's %d items now." % len(stuff) #取stuff长度来判断字符个数
    
print "There we go: ",stuff  

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #列表最后一个元素
print stuff.pop()   #.pop()函数运行在打印所有字符之前。#.pop()函数是将一个LIst里面的最后一个值取出打印,并且返回的时候从List里面删掉。
print ' '.join(stuff) #.join():连接字符串数组。将字符串、元组、列表中的元素以指定的字符（分隔符）连接成一个新的字符串
print '&'.join(stuff[3:5]) #切片，从列表的第三个元素取值，直到第5个元素，不包含第5个并用“&”连接
    