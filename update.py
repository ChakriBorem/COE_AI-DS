import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
print(mydb)
cur = mydb.cursor()
city = input("Enter city")
cur.execute("update employee set esal=esal+3000 where city=%s", (city,))
print("Table updated")
mydb.commit()
