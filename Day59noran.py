#Python RegEx3 The sub() function
import re
#Replace all white-space charcters with the digit "9":
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
#Replace the first two occurrences of a white-space charcters with the digit "9":
x = re.sub("\s", "9", str, 2)
print(x)
#Match object, Do a search() function returns a match object:
x = re.search("ai", str)
print(x)
#search for an upper case "S" character in the beginning of a word, and print its position:
x = re.search(r"\bS\w+", str)
print(x.span())

x = re.search(r"\bS\w+", str)
print(x.string)

x = re.search(r"\bS\w+", str)
print(x.group())