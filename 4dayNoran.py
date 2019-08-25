#Example1

x=2 #int
y=3.8 #float
z= 1j #complex
print (type(x))
print(type(y))
print(type(z))

#Example2 Int
i= 2
x= 68768464983164893
y=-27856
print (type(i))
print(type(x))
print(type(y))

#Example3 Float
i=2.20
j=2.3
z=-22.99
print (type(i))
print(type(j))
print(type(z))

x= 25e2
y= 21E5
d= -65.4e98
print (type(x))
print(type(y))
print(type(d))

#Example4 Complex
i= 2+6j
x= 6j
y= -6j
print (type(i))
print(type(x))
print(type(y))


#Example5 Convert
x=2 #int
y=3.8 #float
z= 2j #complex

#convert from int to float:
a= float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c=complex(x)

print(a)
print(b)
print(c)

print (type(a))
print(type(b))
print(type(c))


#Example6

import random
print (random.randrange(1,10))
