#python tuples 2
#check if item exists
tuples = ("red", "green", "yellow")
if "red" in tuples:
    print ("Yes, 'red' is in the color tuples")
#Repeat Item
i = ("Python")*4
print(i)
j = ("Python",)*4
print (j)
#Operator in Tuple
tuple1 = (1,2,3,4)
tuple2 = (5,6)
tuple = tuple1 + tuple2
print (tuple)
x = (3,4,5,6)
x = x + (1,2,3)
print (x)
#Tuple Length
z = ("cherry", "orange", "green apple")
print (len(z))
#the tuple() Contructor
x = tuple(("white", "Pink", "blue")) #note the double round-brackets
print(x)
thislist = [3, 4, 5, 6,"T", "N"]
thistuple = tuple(thislist)
print(thistuple)
