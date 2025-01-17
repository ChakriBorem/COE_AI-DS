import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
cur = mydb.cursor()
cur.execute("create table employee(eid int,ename varchar(20),esal int,city varchar(20));")
print("Employee table created")
mydb.commit()
