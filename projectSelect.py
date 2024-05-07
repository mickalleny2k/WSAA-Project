import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="simonproject"
)

cursor = db.cursor()
sql="select * from project where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

db.close()
cursor.close()

