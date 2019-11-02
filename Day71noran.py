#Python MySQL2
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1010",
    database="mydatabase"
)

mycursor = mydb.cursor()

#val = [
#    ('Peter' , 'Lowstreet 4'),
#    ('Amy' , 'Apple st 652'),
#   ('Richard' , 'Sky st 331'),
#   ('Susaan' , 'one way 98'),
#   ('Wiliam' , 'Central st 989'),
#   ('Viola' , 'Sideway 1633')
# ]
#mycursor.executemany(sql, val)
#mydb.commit()
#print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21 ") #like a tuple
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)


mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#mycursor.execute("SELECT * FROM customers")
#result = mycursor.fetchone()
#print(result)

sql = "SELECT * FROM customers WHERE address = 'Sky st 331'"

sql = "SELECT * FROM customers WHERE address Like '%way%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for z in myresult:
    print(z)


