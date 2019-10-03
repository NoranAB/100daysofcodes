#Python Inhertiance 2
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def Printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year #Add Properties
    def Welcome(self): #Add Methods
        print("Welcom", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("John", "Mike", 2019)
x.Printname()
#Add Properties
print(x.graduationyear)
#Add Methods
x.Welcome()