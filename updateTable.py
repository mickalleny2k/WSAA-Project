import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="simonproject"
)

cursor = db.cursor()
sql="update project set staff=%s where id = %s"
id = input ("Enter id: ")
staff = input ("Enter staff: ")

cursor.execute(sql, (staff,id))

db.commit()
print("update done")

cursor.close()
db.close()
