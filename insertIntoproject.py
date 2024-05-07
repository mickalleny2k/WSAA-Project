import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="simonproject"
)

cursor = db.cursor()
sql="insert into project (id,name,staff) values (%s,%s,%s)"
id = input ("Enter id: ")
name = input ("Enter name: ")
staff = input ("Enter staff: ")
values = (id,name,staff)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()