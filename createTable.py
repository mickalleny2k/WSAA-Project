import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="simonproject"
)

cursor = db.cursor()
sql="CREATE TABLE project (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), staff INT)"
cursor.execute(sql)

db.close()
cursor.close()