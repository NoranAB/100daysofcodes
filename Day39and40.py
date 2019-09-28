#Recursion
def recursion(i,j):
    if (j==0):
        return 1
    else:
        return i*recursion(i,j-1)
print(recursion(5,3))

#Lambda
lists = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
numbers = list(filter(lambda z: (z >0), lists))
print(numbers)


