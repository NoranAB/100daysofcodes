#Python Functions - creating a function
def my_function():
    print("Hello from a function")

my_function()
#Parameters
def the_function(fname):
    print(fname + " Refsnes")

the_function("Email")
the_function("Tobias")
the_function("Linus")
#Defualt parameter value
def function (country = "Norway"):
    print("I am from " + country)

function("Sweden")
function("Italy")
function()
function("Brazil")
