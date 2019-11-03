#task1
i= open("text1file.txt", "r")
print(i.read())
i.close()

j = open("text2file.txt", "a")
j.write("The best way we learn anything is by practice and exercise questions")
j.close()
j = open("text2file.txt", "r")
print(j.read())


#task2

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1010",
    database="mydatabase"
)
mycursor = mydb.cursor()

#Create the table:
#table = 'CREATE TABLE Employee(ID INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(100), LastName VARCHAR(100), Age INT, Gender VARCHAR(20), Salary INT)'
#mycursor.execute(table)

#Insert Value:
sql = 'INSERT INTO Employee(FirstName, LastName, Age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)'
val = [
    ("Ahmed", "Ali", 30, "Male", 10000),
    ("Khalid", "Muhammad", 34, "Male", 7000),
    ("Norah", "Saleh", 29, "Female", 7000),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")
sql = 'SELECT * FROM Employee'
mycursor.execute(sql)

myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)

print("Show FirstName, Gender And Salary")
sql = 'SELECT FirstName, Gender, Salary FROM Employee'

print("Sort By FirstName")
sql = 'SELECT * FROM Employee ORDER BY FirstName DESC'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)

print("Delete Record")
sql = 'DELETE FROM Employee WHERE Age = %s'
age = 34,
mydb.commit()
mysql = 'SELECT * FROM Employee'
mycursor.execute(sql, age)
mycursor.execute(mysql)
myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)