import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="simonproject"
)

cursor = db.cursor()
sql="delete from project where id = %s"
id = input ("Enter the ID you wish to delete: ")
#value = 1

cursor.execute(sql,(id,))

db.commit()
print("delete done")

db.close()
cursor.close()