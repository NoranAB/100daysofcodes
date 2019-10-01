#Python Classes and Objects
class MyClass:
    x = 5
print(MyClass)
#Create Object
class MyClass1: #تعريف الصنف
    y = 8       # انشاء متغير بداخل الصنف
p1 = MyClass1() #إنشاء كائن لهذا الصنف
print(p1.y)     # الوصول إلى متغير وطباعة قيمته
#The__init__()Functione
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
z = Person("John", 36)
print(z.name)
print(z.age)
#The self Parameter
class myclasses:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name )
i = myclasses("Reem", 23)
i.myfunc()
