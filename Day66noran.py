#Python String Formatting 2
quantity = 4
itemno = 626
price = 62
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
age = 34
name = "Mohammad"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
order = "I have a {carname}, it is a {model}."
print(order.format(carname = "Audi", model = 2019))