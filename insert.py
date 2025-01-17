import mysql.connector as c
mydb = c.connect(
  host="localhost",
  user="root",
  password="manager",
  database="dbconnect"
)
cur = mydb.cursor()
id = input("Enter eid:")
name = input("Enter ename:")
sal = input("Enter esal:")
city = input("Enter city")
cur.execute("insert into employee values(%s,%s,%s,%s)", (id, name, sal, city))
mydb.commit()
