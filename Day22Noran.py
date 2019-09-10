#Python Dictionaries
x1 = {}
print(x1)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "years": 1994
    } #dictionary name = {keys: values}
print(thisdict)
x2 = thisdict["model"]
print(x2)
x3 = thisdict["years"]
print(x3)
x = thisdict.get("brand")
print(x)
#Example2 Change Values
dict = {
    "language": "Python",
    "topic": "saudidevorg",
    "years": 2019
}
dict["years"] = 2020
print(dict)
#Example3 Loop through a dictionary
y = {
    "language1": "Python",
    "language2": "Javascript",
    "language3": "Swift"
}
for z in y:
    print(z) #print all key names in the directionary, one by one
y1 = {
    "language1": "Python",
    "language2": "Javascript",
    "language3": "Swift"
}
for z1 in y1:
    print(y1[z1])#print all values in the directionary, one by one
i = {
    "univ1": "SEU",
    "univ2": "KSU",
    "univ3": "KFU",
    "years": 2030
}
for j in i.values():
    print(j)
mydict = {"univ1": "SEU", "univ2": "KFU", "years": 2030 }
print(mydict.values())
dictionary = {
    "univ1": "SEU",
    "univ2": "KSU",
    "univ3": "KFU",
    "years": 2030
}
for dict1, dict2 in dictionary.items():
    print(dict1, dict2)
z1 = {"language1": "Chinese", "language3": "Italia", "years": 1996}
print(z1.items())