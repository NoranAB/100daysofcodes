#Python Loop 3 The range() Function
for x in range (6):
    print(x)
for y in range (2,6):
    print(y)
for z in range (2,30,3):
    print(z)
for r in range (8):
    print (r)
else:
    print("Finally finished!")
#Nested Loops
i = ["blueberry", "raspberry", "cherry"]
j = ["blue", "pink", "red"]

for i1 in i: #outer loop
    for j1 in j: #Inner loop
        print(i1,j1)