import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='228928125',
    database='tester'
)

mycursor = mydb.cursor()
mycursor.execute("create table tablle(id int, name VARCHAR(255))")

mycursor = mydb.cursor()
sql = "insert into tablle(id, name) values(%s, %s)"
val = (1, "Alex")

mycursor.execute (sql,val)
mydb.commit()

mycursor.execute("select * from tablle")
result = mycursor.fetchall()
print(result)

mycursor.execute("UPDATE `tablle` set name = 'Mars' WHERE name = 'Alex'")
result = mycursor.fetchall()
mydb.commit()
