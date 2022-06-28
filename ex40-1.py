#############class汇总：

1. class X(Y): 创建一个叫X的类，它是Y的一种

2. class X(object): def __init__(self, J): 类X有一个__init__接受self和J为其中的参数。

3. class X(object): def M(self,J): 类X有一个函数名称为M，它接受self和J作为参数。

4. foo = X():将foo设为类X的一个实例。

5. foo.M(J): 从foo中找到M函数，并使用self和J参数调用。

6. foo.K = Q：从foo中获取K属性，并将其设为Q。