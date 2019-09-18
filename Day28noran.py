#Python Loops while loop
i = 1 #intialization
while i < 7: #condition
    print(i) #statement
    i += 1 #increment
#the break statement , mean stop the loop
j = 1
while j < 7:
    print(j)
    if j==3:
        break
    j += 1
#the continue statement
z = 0
while z < 6:
    z += 1
    if z == 3:
        continue #to skip the loop and continue the next
    print(z)
#the else statement
x = 1
while x < 6:
    print (x)
    x += 1
else:
    print("x is no longer less than 6")
y = 10
while y < 6:
    print (y)
    y += 10
else:
    print("y is no longer less than 6")