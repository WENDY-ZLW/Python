#This python file uses the following encoding:utf-8
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')    #.split() 通过指定分隔符对字符串进行切片。如果参数 num 有指定值，则分隔num+1个子字符串
    return words                # str.split(str="", num=string.count(str))：(以what为分隔符，分成几个）；line 3：以空格为分隔符

def sort_words(words):          #排序
    """Sorts the words."""
    return sorted(words)        #sort是应用在list上的方法，sorted()可以对所有可迭代的对象进行排序操作。内建函数sorted方法返回的是一个新的 list
    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)         #.pop(0)为移除列表第一个元素，并且返回值为此元素
    print word
    
def print_last_word(words):
    """Prints the last word after poppint it off."""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Take in a full sentene and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the firstand last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)