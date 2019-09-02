#Data Structure
#Example1 python lists []
x=[]
numbers=[1,2,3,4,5,6]
colors=["blue", "black", "white"]
lists=["python", 100, "day"]
thislist=[2.2, 6,8]
print(x)
print(numbers)
print(colors)
print(lists)
print(thislist)

#Example2 Access Items - use Index number to access th list items
x= ["white", "blue", "red"]
print(x[1])
print(x[2])
print(x[0])

#Example3 Loop through a list
thislist = ["burger", "pizza", "salad"]
for i in thislist:
    print(i)
list = [2, 4.9, 6, 8.2]
for j in list:
    print(j)

#Example4 Change Item Value
fruit= ["blackberry", "mango", "roseberry"]
fruit[1] = "blueberry"
print(fruit)
del fruit[1]
print(fruit)
