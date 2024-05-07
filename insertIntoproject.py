import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="simonproject"
)

cursor = db.cursor()
sql="insert into project (id,name,staff) values (%s,%s,%s)"
values = (1,"Education and Training",10)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()