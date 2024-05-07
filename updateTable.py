import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="simonproject"
)

cursor = db.cursor()
sql="update project set name= %s, staff=%s"
values = ("E & T",9)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()
