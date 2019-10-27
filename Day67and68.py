#Task1
print("Enter the first letter of your name:")
i = input()
print("Enter the last letter of your name:")
j = input()
name = "Your first litter name with {} and the last letter with {}."
print(name.format(i[0], j[0]))

#task2
first = "Ahmed"
last = "Ali"
balance = 53.44
txt = "Dear {} {}, Your current balance is {:.2f}$"
print(txt.format(first, last, balance))