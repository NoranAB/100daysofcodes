#Python RegEx2
import re
#return a list containing every occurrence of "ai":
str = "The rain in spain"
x = re.findall("ai", str)
print(x)
#check if "portugal" is in the string:
x = re.findall("Portugal", str)
print(x)
if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
#The search() function
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())

x = re.search("Portugal", str)
print(x)
#The split() function
#split the string at every white-space charcter:
x = re.split("\s", str)
print(x)