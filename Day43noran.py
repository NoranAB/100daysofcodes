#Python Inheritance
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
#Use the person class to create an object, and then excute the printname method:
x = person ("John", "Done")
x.printname()
#Create a child class
class child:
    def __init__(self, fname1, lname1):
        self.firstname1 = fname1
        self.lastname1 = lname1
    def printname(self):
            print(self.firstname1, self.lastname1)
class Student(child):
    pass
y = Student("Mike", "Olsen")
y.printname()
#Add the__init__() Function
class firststudent:
    def __init__(self, name1, name2): #add properties etc.
        self.name1first = name1
        self.name2last = name2
    def printname1(self):
        print(self.name1first, self.name2last)
class person(firststudent):
    def __init__(self, name1, name2):
        firststudent.__init__(self, name1, name2)
z = person("John", "JoJo")
z.printname1()