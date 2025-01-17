import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="dbconnect"
)
print(mydb)
cur = mydb.cursor()
id = input("Enter your id")
cur.execute("delete from employee where eid=%s;", (id,))
print("Record deleted")
mydb.commit()
