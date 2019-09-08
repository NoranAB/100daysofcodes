#Python Sets
#Example1 Empty set
x = {"python", "swift", "javascript"} #set are unordered
print(x)
y = {"Reem", "Reem", 2,4,6,4} #not repeat item
print(y)
#Example2 Access Items (loop)
i = {"cherry", "green apple", "mango"}
for z in i:
    print (z)
j = {"Macbook", "HP", "Toshipa"}
print ("Macbook" in j)
#Example3 change items add, update
thisset = {"Arabic", "English", "chinese"}
thisset.add("French") #add one item to a set
print(thisset)
thissets = {"English", "French", "Chinese"}
thissets.update(["Arabic", "Japanese", "Italian"])
print(thissets)
