#File Handling
f = open("demofile.txt")
z = open("demofile.txt", "rt")
h = open("demofile.txt", "r")
#the code above is the same as
print(f.read())
print(z.read(6))
print(h.readline())
print(h.readline()) #by calling readline() two times, you can read the two first lines.

i = open("demofile.txt", "r")
for x in i:
    print(x)
print(i.readline())
i.close()

#Write to an exiting fie demofile2
j = open("demofile2.txt", "a")
j.write("Now the file has more content!")
j.close()


j = open("demofile2.txt", "r")
print(j.read())

#demofile3
e = open("demofile3.txt", "w") #the "w" method will overwrite the entire file
e.write("Woops! I have deleted the content!")
e.close()

e = open("demofile3.txt", "r")
print(e.read())

#myfile , create a new file
y = open("myfile.txt", "w")