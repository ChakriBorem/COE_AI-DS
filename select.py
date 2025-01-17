import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
print(mydb)
cur = mydb.cursor()
print("Employee details")
cur.execute("select *from employee")
emp = cur.fetchall()
for i in emp:
    print(i)
print()
print("Employee details in ascending order of their names ")
cur.execute("select *from employee order by ename")
std = cur.fetchall()
for i in std:
    print(i)
print()
print("Employee details whose salary is in between 8000 and 90000")
cur.execute("select *from employee where esal between 80000 and 90000")
std = cur.fetchall()
for i in std:
    print(i)
print()
print("Employee details whose city is Hyderabad")
cur.execute("select *from employee where city='Hyderabad'")
std = cur.fetchall()
for i in std:
    print(i)
print()
mydb.commit()
