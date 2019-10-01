#Python Classes and objects2
#Object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("JoJo", 34)
p1.myfunc()
#Modify Object Properties
class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
x = myclass("JoJo", 34)
x.age = 44
print(x.age)
#Delete Object Properties (del)
class myclasses:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
z = myclasses("JoJo", 34)
del z.age
print(z.age) #AttributeError
#Delete objects
class persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
y = persons("John", 45)
del y
print(y) #NameError