#Example1  String format لايمكن دمج متغير نصي مع متغير رقمي
age = 34
txt = "My name is Rayn, I am " + age
print (txt)

#Example2   .Formate() , {}اجراء تنسيق على النص
age = 34
txt = "My name is Rayn, and I am {}"
print (txt.format(age))

#Example3  arguments{} عدد غير محدود
quantity = 4
itemno = 643
price = 52.55
myorder = " I want {} peices of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Example4 .format() {} تنسيق النص اكثر من مره .ترقيم المدخلات index number
quantity = 6
itemno = 657
price = 75.22
myorder = " I want to pay {1} dollars for {0} pieces of item {2}."
print (myorder.format(quantity, itemno, price))