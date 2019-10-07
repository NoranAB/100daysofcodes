#Python Scope
#Local scope
def myfunc():
    x = 224
    print (x)
myfunc()
#Function Inside Function
def func():
    z = 624
    def myinnerfunc():
        print (z)
    myinnerfunc()
func()
#Global Scope
y = 400
def thefunc():
    print(y) #local
thefunc()
print(y) #global