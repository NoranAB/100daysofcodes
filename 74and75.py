#task1
i= open("textfile.txt", "r")
print(i.read())
i.close()

j = open("text1.txt", "a")
j.write("The best way we learn anything is by practice and exercise questions")
j.close()
j = open("text1.txt", "r")
print(j.read())


#task2