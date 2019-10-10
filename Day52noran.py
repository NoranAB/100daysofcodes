#Python Datetime
import _datetime
x = _datetime.datetime.now()
print(x)

import _datetime
y = _datetime.datetime.now()
print(y.year)
print(y.strftime("%A"))

#Creting Date Objects
import _datetime
z = _datetime.datetime(2020, 6, 16)
print(z)

#The Strftime() Method
import _datetime
i = _datetime.datetime(2019, 3, 15)
print(i.strftime("%B"))
print(i.strftime("%b"))