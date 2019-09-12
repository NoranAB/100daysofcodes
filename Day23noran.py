#Python Dictionaries 2
#check if Key Exists
thisdict = {
    "Company1": "DHL",
    "Company2": "UPS",
    "year": 2020
}
if "Company1" in thisdict:
    print("Yes, 'Company2' is one of the keys in the thisdict directionaty")
#Dictionary Length, number of items
x1 = {
    "language1": "Italian",
    "language2": "Chinese",
    "language3": "French",
    "year": 2020
}
print(len(x1))
#Adding Items
x2 = {
    "brand": "BMW",
    "color": "black"
}
x2["year"] = 2019
print(x2)
#Removing Items
y = {
    "language1": "Python",
    "language2": "Swift",
    "language3": "javascript",
    "language4": "PHP"
}
y.pop("language2")
print(y)
y.popitem()
print(y)
del y["language3"]
print(y)
y.clear()
print(y)
del y
print(y)