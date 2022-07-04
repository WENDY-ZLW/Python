#This python file uses the following encoding:utf-8
def break_words():
    stuff = """This function will break up words for us."""
    words = stuff.split(' ')   
print break_words()    #漏写return语句会返回return

#TypeError: break_words() takes exactly 1 argument (0 given) #TypeError: break_words() 只需要1个参数(给定0个)

def break_words():
    stuff = """This function will break up words for us."""
    words = stuff.split(' ')    #.split() 通过指定分隔符对字符串进行切片。如果参数 num 有指定值，则分隔num+1个子字符串
    print words    

break_words()    