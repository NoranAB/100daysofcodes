#Data structure - python lists3 - list methods

#Example1 List Length - len()
z = ["python", "javascript", "PHP"]
print (len(z))

#Example2 Add Items to the end of the list - append()
x = ["swift", "Javascript", "MicroBit"]
x.append("Python")
print(x)

#Example3 add Items at the specified index, insert()
i = ["swift", "PHP", "MicroBit"]
i.insert(0, "Python")
print(i)

#Example4 remove()
thislist = ["blue", "black", "python"]
thislist.remove("python")
print(thislist)

#Example5 pop()
list = ["Python", "Javascript", "Swift"]
list.pop()
print(list)
list.pop(1)
print(list)

#Example6 clear()
j = ["cherry", "apple", "orange"]
j.clear()
print(j)

#EXample7 Copy a List
z = ["Python", "Javascript","Swift"]
x=z.copy()
z.pop(0)
print(x)
print(z)

x = ["Python", "Javascript","Swift"]
y=z
x.pop(0)
print(y)
print(x)

thislist = ["apple", "banana", "cherry"]
mylist = list (thislist)
print (mylist)