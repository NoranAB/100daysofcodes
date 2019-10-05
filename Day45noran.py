#Python Iterators
mytuple = ("cherry", "orange", "apple")
myit = iter(mytuple)
print(next(myit)) #next() give next value in every time it's called
print(next(myit))
print(next(myit))

mystr = "blueberry"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping Through an Iterator
mytuple = ("blue", "pink", "red")
for x in mytuple:
    print(x)

#Create an Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#StopIteration
class Numbers:
    def __iter__(self):
        self.z = 1
        return self
    def __next__(self):
        if self.z <= 20:
            y = self.z
            self.z += 1
            return y
        else:
            raise StopIteration
class1 = Numbers()
myiter = iter(class1)
for y in myiter:
    print(y)
