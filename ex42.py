#This python file uses the following encoding:utf-8
##Animal is-a object (yes, sort of confusing) look at the extra credit
##类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()#将t设为类Test的一个实例。
t.prt()   #从t中找到prt函数，并且调用。

 #<__main__.Test instance at 0x0000000002EE2F08> ：从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址。
 #__main__.Test ：self.__class__ 则指向类。
 
class Employee:
   empCount = 0
 
   def __init__(self, name, salary,age):  #初始化，self为一个实例
      self.name = name                #从self中获取name属性，并将其设为name
      self.salary = salary
      self.age = age
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary, "Age:",self.age
 

emp1 = Employee("Zara", 2000,9)       #self不设置参数
emp2 = Employee("Manni", 5000,12)
emp1.displayEmployee()              #从emp1中找到displayEmployee函数，并且调用它
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

############可以使用以下函数的方式来访问属性：
"""getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性
"""

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'

##########Python内置类属性:
"""
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__