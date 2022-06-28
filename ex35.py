# This Python file uses the following encoding: utf-8
from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0) #终止程序
    else:
        dead("You greedy bastard!")
  
  
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False    #首先规定bear_moved为False,即可跳出循环。
    
    while True:#（如果没有Flase将一直输入）；任意检测到false会跳出循环，否则将一直无限循环，所以要加and将一直输入）；
        next = raw_input("> ")     
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved: #必须输入open door并且bear_moved为true才可以进入gold_roon
            gold_room()
        else:#输入open door但bear_moved为False算作“else”
            print "I got no idea what that means."
        

def cthulhu_room():
    print """
Here you see the great evil Cthulhu.
He,it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?
    """
    next = raw_input("> ")
    
    if "flee" in next: #if语句必须包含一个else；嵌套不要超过两层（最好移至另一个函数）
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):#死亡原因（while true）+Good job；why为dead()函数的变量
    print why, "Good job!" #print xx，“xxx”为一句话！
    exit (0)  #终止程序
    
def start():
    print """
You are in a dark room.
There is a door to your right and left.
Which one do you take?
    """
    next =  raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()

    
        
        

         