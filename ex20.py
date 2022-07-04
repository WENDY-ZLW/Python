#This file uses the following encoding:utf-8
from sys import argv
script,input_file = argv

def print_all(f):
    print f.read() #.read() 每次读取整个文件，它通常将读取到底文件内容放到一个字符串变量中，也就是说 .read() 生成文件内容是一个字符串类型。
    
def rewind(f):
    f.seek(0)  #.seek() 方法用于移动文件读取指针到指定位置。fileObject.seek(offset[, whence])
               #offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
               #whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    
def print_a_line(line_count,f):
    print line_count, f.readline()  #.readline()每只读取文件的一行，通常也是读取到的一行内容放到一个字符串变量中，返回str类型。（扫描字节，直到找到\n, f会记录每次读取到的位置)
                                    #.readlines()每次按行读取整个文件内容，将读取到的内容放到一个列表中，返回list类型。
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file) #将指针重新定回到文件的开头

print "Let's print three lines:"

#for i in range (1,4):
#    print_a_line(i,current_file)

i=1 
#while i < 4: 
#   print_a_line(i,current_file)    
#   i += 1

while 1:
    print_a_line(i,current_file)  
    i+=1
    if i > 3:
        break
    
#while 语句时还有另外两个重要的命令 continue，break 来跳过循环。
#continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，例while 1：