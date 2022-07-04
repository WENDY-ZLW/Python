#This file uses the encoding: utf-8
def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b
    
def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a * b
    
def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a / b
    
    
print "Let's do some math with just functions!"

#一定要加 float(raw_input())// int(raw_input())。这样输出才能用%d，才可以证明是num，不然返回的是str则不能运行。
age = float(raw_input("> age: "))
height = float(raw_input("> height: "))
weight = float(raw_input("> weight: "))
iq = float(raw_input("> iq: "))

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print "That becomes: " ,what, "Can you do it by hand?"

    
