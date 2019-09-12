#Example1 copy()
i = {
    "language1": "MicroBit",
    "language2": "PHP",
    "year": 2019
}
i1 = i.copy()
print(i1)
j = {
    "language1": "Japanese",
    "language2": "French",
    "language3": "English"
}
j1 = dict(j)
print(j1)
#Example2 Nested Dictionaries (many dictionaries)
myfamily = {
    "child1": {
        "name": "Emil",
        "year":2006
    },
    "child2": {
        "name": "John",
        "year": 2008
    },
    "child3": {
        "name": "Rayn",
        "year": 2010
    }
    }
print(myfamily)
child3 = {
        "name": "Emil",
        "year":2012
    }
child4 = {
        "name": "John",
        "year": 2016
    }
child5 = {
        "name": "Rayn",
        "year": 2018
    }
family = {
    "child3": child3,
    "child4": child4,
    "child5": child5
}
print(family)
#The dict() Constructor
thisdict = dict(car1= "maserati", car2="porsche", year=2020)
#note that keywords are not string litrals
#note the use of equals rather than colon for the assignment
print(thisdict)