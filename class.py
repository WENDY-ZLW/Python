###################class汇总：

1. class X(Y): 创建一个叫X的类，它是Y的一种

2. class X(object): def __init__(self, J): 类X有一个__init__接受self和J为其中的参数。

3. class X(object): def M(self,J): 类X有一个函数名称为M，它接受self和J作为参数。

4. foo = X():将foo设为类X的一个实例。

5. foo.M(J): 从foo中找到M函数，并使用self和J参数调用。

6. foo.K = Q：从foo中获取K属性，并将其设为Q。



####################Python类中的实例属性与类属性：
> 类的属性是用来表明这个类是什么的。类的属性分为实例属性与类属性两种。
> 区别：实例属性每个实例都各自拥有，相互独立；而类属性有且只有一份，是共有的属性。

#####################实例属性：
1....................实例属性用于区分不同的实例；

类的属性都是用来指明这个类"是什么"，实例属性是用来区分每个实例不同的基础。

E.g......在上面我们创建了Circle类，所有圆都具备半径这个通用属性，下面我们为circle1、circle2 圆实例添加半径 r 这个属性并赋值。

circle1.r = 1  # r为实例属性
circle2.R= 2  
print(circle1.r)  # 使用实例名.属性名可以访问我们的属性
print(circle2.R)

circle1.r、circle2.R 大小写有区分，两个实例的属性名称不统一不利于后面的访问和使用，而且每次在创建圆后我们要再为实例添加属性会比较麻烦.
所以我们可以在创建实例时给类初始属性。
在定义 Circle 类时，可以为 Circle 类添加一个特殊的 __init__() 方法，当创建实例时，__init__() 方法被自动调用为创建的实例增加实例属性。

class Circle(object):  # 创建Circle类
   def __init__(self, r): # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
       self.r = r  # 表示给我们将要创建的实例赋予属性r赋值



#######################类属性：
2......................类属性是每个实例的共有属性:

绑定在实例上的属性不会影响其他实例，但类本身也是一个对象。
如果在类上绑定属性，则所有实例都可以访问该类的属性，并且所有实例访问的类属性都是同一个！！！
记住，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

E.g......圆周率π为圆的共有属性，可以在Circle类添加pi这个类属性，如下：

class Circle(object):
   pi = 3.14  # 添加类属性

   def __init__(self, r):  #class Circle 中有__init__函数，并且参数为self和r。
       self.r = r          #从self中获取r属性,并且设定为r。

circle1 = Circle(1)
circle2 = Circle(2)
print('----未修改前-----')
print('pi=\t', Circle.pi)    # “\t” 为Tab键，空4格
print('circle1.pi=\t', circle1.pi)  #  3.14
print('circle2.pi=\t', circle2.pi)  #  3.14
print('----通过类名修改后-----')

Circle.pi = 3.14159  # 通过类名修改类属性，所有实例的类属性被改变
print('pi=\t', Circle.pi)   #  3.14159
print('circle1.pi=\t', circle1.pi)   #  3.14159
print('circle2.pi=\t', circle2.pi)   #  3.14159
print('----通过circle1实例名修改后-----')

circle1.pi = 3.14111   # 实际上这里是给circle1创建了一个与类属性同名的实例属性，注意这里为小写“c”
print('pi=\t', Circle.pi)     #  3.14159
print('circle1.pi=\t', circle1.pi)  # 实例属性的访问优先级比类属性高，所以是3.14111   
print('circle2.pi=\t', circle2.pi)  #  3.14159
print('----删除circle1实例属性pi-----')

通过类创建的实例修改的类属性后，通过其他实例访问类属性他的值还是没有改变。
其实是通过实例修改类属性是给实例创建了一个与类属性同名的实例属性而已，
实例属性访问优先级比类属性高，所以我们访问时优先访问实例属性，它将屏蔽掉对类属性的访问




#######################类的使用方法：

在类的内部，使用 def 关键字来定义方法，与一般函数定义不同.
类方法必须第一个参数为 self, self 代表的是类的实例（即你还未创建类的实例），其他参数和普通函数是完全一样。

> E.g...我们给圆类 Circle 添加求面积的方法 get_area ：

class Circle(object):
   pi = 3.14  # 类属性

   def __init__(self, r):
       self.r = r  # 实例属性

   def get_area(self):
       """ 圆的面积 """
      #return self.r**2 * Circle.pi # 这个pi为类属性的值..通过实例修改pi的值对面积无影响.
       return self.r**2 * self.pi  # 通过实例修改pi的值对面积我们圆的面积就会改变

circle1 = Circle(1)
print(circle1.get_area())  # 调用方法 self不需要传入参数，不要忘记方法后的括号  输出 3.14