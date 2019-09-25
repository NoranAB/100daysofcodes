#Python Functions 2
#Passing a list as a Parameter
def my_function(food):
    for x in food:
        print(x)
fruits = ["cherry", "orange", "apple"]
my_function(fruits)
#Return Values
def the_function (y):
    return 5* y

print (the_function(3))
print (the_function(5))
print (the_function(9))

#Keyword Arguments (kwargs)
def the_functions (child3, child2, child1):
    print("The youngest child is " + child3)
the_functions (child1 = "Emil", child2 = "Tobias", child3 = "Linus") #the key=value syntax

#Arbitrary Arguments
def my_functions (*kids):
    print("The youngest child is " + kids[2])
my_functions ("Tom", "Rayn", "Ken")

#Recursion
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print ("\n\nRecursion Example Results")
tri_recursion(6)