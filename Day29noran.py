#Python Loops2
fruits = ["cherry", "blueberry", "Raspberry"]
for x in fruits:
    print(x)
#Looping through a string
for x in "blueberry":  #loop through the letters in the word
    print(x)
#The Break statement
Languages = ["Python", "Javascript", "Swift"]
for y in Languages:
    print(y)
    if y== "Javascript":
        break
Language = ["PHP", "Microbit", "Swift"]
for i in Language:
    if i== "Microbit":
        break
    print(i)
#The continue Statement
j = ["blueberry", "raspberry", "blackberry"]
for z in j:
    if z=="raspberry":
        continue #don't print raspberry
    print(z)