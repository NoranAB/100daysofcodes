#Python MySQL
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1010",
    database="mydatabase"
)


mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(225), address VARCHAR(225))")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#  print(x)

