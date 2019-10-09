#Python Modules2
import mymodule2 as mx

a = mx.person2["age"]
print(a)
#Built-in Modules
import platform
print(platform.python_version())

#using the dir() function
import platform
x = dir(platform)
print(x)

from mymodule2 import person2
print (person2["country"])