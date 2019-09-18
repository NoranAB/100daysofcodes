#Conditional Statements / If...Else
a = 22
b = 222
if b > a: #colon is a code block
    print("b is greater than a") #must be whitespace
#Indentation (whitespace at the beginning of a line (4blocks)
#elif (mean if and else)
i = 25
j = 25
if j > i:
    print("j is greater than i")
elif i==j:
    print("i and j are equal")
#else when elif condition is not true we use else condition
x = 400
y = 44
if y > x:
    print("y is greater than x")
elif x==y:
    print("x and y are equal")
else:
    print("x is greater than y")
#we can also have an else without the elif
n = 200
r = 22
if r > n:
    print ("r is greater than n")
else:
    print("r is not greater than a")
#Short Hand If , put at the same line
a1 = 400
a2 = 66
if a1 > a2: print ("a1 is greater than a2")
#Short Hand If....Else
b1 = 6
b2 = 600
print("b1") if b1 > b2 else print("b2")
print("b1") if b1 < b2 else print("b2")
x1 = 440
x2 = 440
print("x1") if x1 > x2 else print("=") if x1==x2 else print("x2")
#and ,used to combine conditional statements
i1 = 220
i2 = 22
i3 = 600
if i1 > i2 and i3 > i1:
    print("Both conditions are True")
#Or , uset to combine conditional statements
j1 = 400
j2 = 44
j3 = 660
if j1 > j2 or j1 > j3: #print at least one true
    print("At least one of the conditions is True")
#Nested If / if statement inside if statement
z = 44

if z > 10:
    print("Above ten,")
    if z > 20:
        print("and also above 20!")
    else:
        print("but not above 20. ")