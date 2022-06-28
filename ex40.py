#This file uses the following encoding:utf-8
class Song(object):
    
    def __init__(self,lyrics):  #记住是两个下划线！！！！！  初始化￥；self为多余的函数，即python创建的空对象，可谓他设置变量等。。。
	    self.lyrics = lyrics
		
    def sing_me_a_song(self):
        for line in self.lyrics:
	        print line
             
happy_bday = Song(["Happy birthday to you", 
                   "I don't want to get sued", 
                   "So I'll stop right there"])



bulls_on_parade = Song(["They rally around family", 
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()   #参照书P121 class style！

bulls_on_parade.sing_me_a_song()

#object() takes no parameters:
#这是因为Python在创建对象是，分为两个阶段：第一个阶段，对象是通过调用new方法来创建的.
#new方法并不会立即返回一个对象实例，new方法之后，会调用init方法来给对象增加新的属性。
#对于上面的对象o，调用的就是Python首先查找o的init方法，但是没找到，然后查找父类的init方法，假设父类是上面的Foo，可以方式init方法依然不存在.
#所以最后会找到object的init属性。object的init是存在的，并且是个方法，然后调用这个方法，传入相应的参数，但是object.init方法没有参数，然后我们就得到的上面的错误。












