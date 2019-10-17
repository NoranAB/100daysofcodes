#Python Regular Expressions (RegEx)
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if(x):
    print("Yes! We have a match!")
else:
    print("No match")
i = re.findall("\w", txt)
print(i)
j = re.findall("\s", txt)
print(j)