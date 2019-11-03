#Python MySQL4
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1010",
    database="mydatabase"
)

#UPDATE

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Apple st 652'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

#LIMIT

#mycursor.execute("SELECT * FROM customers LIMIT 4")

mycursor.execute("SELECT * FROM customers LIMIT 4 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor = mydb.cursor()

#JOIN

sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      INNER JOIN products ON users.fav = products.id"
      #LEFT JOIN products ON users.fav = products.id"
      #RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for z in myresult:
    print(z)