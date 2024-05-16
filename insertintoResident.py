import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="simonproject"
)

cursor = db.cursor()
sql="insert into resident (id,name,age,ppsn) values (%s,%s,%s,%s)"
id = input ("Enter id: ")
name = input ("Enter name: ")
age = input ("Enter age: ")
ppsn = input ("Enter ppsn: ")
values = (id,name,age,ppsn)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()