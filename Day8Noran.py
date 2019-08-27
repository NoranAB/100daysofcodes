#Example1 .strip() حذف المسافة الفارغة
b = " Hello, World! "
print (b.strip()) #returns "Hello, World!"

#Example2 len()
x = "Hello, World!"
print(len(x)) #تحسب المسافة الفارغة ايضا

#Example3 .lower()
i= "Hello, World!"
print(i.lower()) #تقوم بترجيع النص بأحرف صغيرة

#Example4  .upper() تقوم بترجيع النص بأحرف كبيرة
j = "Python language"
print(j.upper())

#Example4 .replace() replace ( النص الجديد , النص الاصلي القديم)
x = "Moon Night"
print(x.replace("M", "N"))

#Example5 .splite() مصفوفة نصوص
a = "Hello, World!"
print(a.split(",")) #reurn ['Hello', 'World!']