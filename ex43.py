#This python file uses the following encoding:utf-8
from sys import exit       #from sys import argv可以通过a,b,c,d……=argv来进行批量参数赋值，将argv中的参数依次赋值给左边的变量。
from random import randint #randint()函数属于random模块，必须在函数名称之前先加上random，告诉Python在random模块中寻找这个函数。

class Scene(object):  #Scene的基类，包含了所有场景的通用信息。
    
    def enter(self):
        print "Its subclass enter()"
        exit(1)
        
class Engine(object):
    
    def __init__ (self, scene_map):    #初始化引擎，类Engine有一个__init__，其中的参数有self，scene_map，可以来调用它。
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()   #Map中有参数！！！！！
        
        while True:  #while True 语句中一定要有结束该循环的break语句，否则会一直循环下去.
            print "\n------------"  #Python中while 1，while -2，while x，只要x不等于0，就是条件永远为真，等价于while True，则一直循环。
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(current_scene_name)

  
class Map(object):
    
    scenes = {                                     #dictName = {"key1":func1, "key2":func2, "key3":func3"...}字典的值直接是函数的名字,不用加引号。
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }
           
    def __init__ (self, start_scene):
        self.start_scene =  start_scene
	    
    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)  #dict.get(key[, value]):返回指定键的值。value为没有元素时设置的默认值
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)      

        
class Death(Scene):
    
    emmm = [
        "You died.wakakaak!"
        "sssss"
        "Such a loser~"
        "xxxxxxx smile"
    ]       
    
    def enter(self):
        print Death.emmm[randint(0,len(self.emmm)-1)] #randint(start, stop),都为整数。因为emmm为一个列表，所以取值的元素有0~3，则为len-1.
        exit(1)                                       #注意为中括号！因为为列表；
                                                      #exit(1)表示发生了错误进行退出，而exit(0)则表示程序是正常退出。
    
class CentralCorridor(Scene):
    
    def enter(self):    #return必须写在函数里
        print """
        You are in a new planet! 
        Tell a joke that may let you go!OR ELSE???"
        """
    
        action = raw_input("> ")
    
        if action == "shoot!":
            print "You are dead. Then you will be eaten."
            return 'death'
        
        elif action == "dodge!":
            print "You are dead. your head will be eaten!"
            return 'death'
        
        elif action == " Tell a joke!":
            print "Jump through the Weapon Armory door!"
            return 'laser_weapon_armory'
    
        else:
            print "What do u meam?"
            return 'central_corridor'
        
    
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print "U should get the bomb and the unlock the code."
        print "The code is 3 digits."
        
        code = "%d%d%d" % (randint(0,9),randint(0,9),randint(0,9))  #print(random.randint(1, 9)):大于等于1，小于等于9
        num = raw_input("[keypad]>")
        guesses = 10    #10次机会
        
        while num != code and guesses:
            print "nonono!Try again"
            guesses -= 1
            num = raw_input("[keypad]>")
            
        if num == code:
            print "Congratulations!!!"
            return 'the_bridge'
        
        else:
            print "Oops!U die..."
            return 'death'
        
    
class TheBridge(Scene):
    
    def enter(self):
        action = raw_input("> ")

        if action == "throw the bomb":
            print " it goes off."
            return 'death'

        elif action == "place the bomb":
            print " get off this tin."
            return 'escape_pod'
        
        else:
            print " I don't know what u mean???"
            return 'the_bridge'            
 
 
class EscapePod(Scene):
    
    def enter(self):
        print "Here are 10 pods, choose one that may help you escape!"
        print "Which one do u take?"
        
        good_pod = randint(1,5)
        Num = raw_input("[pod#]> ")
        
        if Num == good_pod:
            print "U jump into a good pod!"
            print "U win!"
            return 'finished'
        
        else:
           print "BYE!"
           return 'death'
  
    
a_map = Map('Central_corridor')   #任务的起点在中央走走廊；a_map为class Map的一个实例
a_game = Engine(a_map)            #运行游戏引擎：1.在地图转到下一个场景 2.获得初始场景 3.进入一个场景
a_game.play()                     #从a_game中调用play函数