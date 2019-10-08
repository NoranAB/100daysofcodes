#Python Scope 2
x = 600  #global
def myfunc():
    x = 400 #local
    print(x)
myfunc()
print(x)
#Global Keyword
def func():
    global y
    y = 440
func()
print(y)

z = 246 #global
def thefunc():
    global z
    z = 468 #تغيير قيمة المتغير العاك z
thefunc()
print(z)