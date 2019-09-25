#Python Lambda 2
def myfunc(n) :
    return lambda a : a * n
mydoubler = myfunc(2)
print (mydoubler(11))
#or use the same function defintion to make a function
def myfunc(z) :
    return lambda y : y * z
mytripler = myfunc(3)
print(mytripler(11))
#or use same function defintion to make both functions
def myfunc(i):
    return lambda j : j * i

mydoubler = myfunc(4)
mytripler = myfunc(6)

print (mydoubler(11))
print(mytripler(11))