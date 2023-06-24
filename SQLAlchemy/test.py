import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="Shop"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM user ")
for _ in mycursor:
  print(_)

if a := 10:
  print(a)
else:
  print(None)




