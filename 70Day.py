#Python MySQL
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1010",
    database="mydatabase"
)

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#  print(x)

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(225), address VARCHAR(225))")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")