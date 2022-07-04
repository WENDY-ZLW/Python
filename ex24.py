# This Python file uses the following encoding: utf-8
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\that do \nnewlines and \t tabs.'
# \'d为 'd   ；  \\为 \  ；  \t为空4个格格  ； \n为转行
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "------------"
print poem
print "------------"

five = 10-2+3-6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates
    

start_point = 10000  #定的名称需要和函数里定义的不同，易混淆！
beans, jars, crates = secret_formula(start_point) #等号是赋值，将return的三个数值赋值分别给beans，jars，crates

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) #多个参数就需要带括号！！！

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)#两种方式写，函数（）可以直接传递jelly—_beans，jars，crates的数值
#也可以将这三个值赋给另外三个变量，然后将变量打印出来.(e.g line 32)