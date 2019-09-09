#Example Set() constructore to make a set
z = set(("school", "univesity")) #note the double round-brackets
print(z)
#Example1
x = {"lemon", "orange", "mint"}
print(len(x))
#Example2 remove, discard item
y1 = {"strawberry", "blueberry", "blackberry"}
y1.remove("blackberry")
print(y1)
y2 = {"strawberry", "blueberry", "blackberry"}
y2.discard("strawberry")
print(y2)
#Example3 pop()
i = {"Twitter", "Instagram", "Snapchat"}
i1 = i.pop()
print(i1) #العنصر الذي تم اختياره للحذف
print(i) # الكود بعد حذف العنصر
#Example4 clear() method empties the set
j1 = {"E-business", "E-commerce", "E-marketing"}
j1.clear()
print(j1)
#Example5 del() keyword will delete the set completely
j2 = {"E-marketing", "E-business", "E-commerce"}
del j2
print(j2) #this will raise an error because the set no longer exists