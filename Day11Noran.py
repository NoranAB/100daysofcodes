#pythone operators 2

#Example1
x = 7
print (x>2 or x<6)
y = 8
print ( y<4 and y>9)

#Example2
i = ["blue", "black"]
j = ["blue", "black"]
z = i
print (i is not z)
#returns false because z is the same object as i

print (i is not j)
#returns true becuase i is not the same object as j, even if they have the same content

print ( i != j)
# to domonetrate the difference between "is not" and *!=": this comparsion returns false because i is equal to j

#Example3 python membership operators  عوامل البحث للمصفوفات
x = ["pink", "white"]
print ("white"in x)
#returns true because a sequence with the value "white" is in the list
print ("pink" not in x )

