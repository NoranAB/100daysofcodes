#Python String Formatting
price = 52
txt1 = "The price is {} dollars"
txt2 = "The price is {:.2f} dollars"
print(txt1.format(price))
print(txt2.format(price))
quantity = 2
itemno = 522
price = 56
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))