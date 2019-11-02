#Python MySQL3
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1010",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

sql = "DELETE FROM customers WHERE address = 'Sideway 1633'"
mycursor.execute(sql)
mydb.commit() #timportant to make the changes
print(mycursor.rowcount, "record(s) deleted")

