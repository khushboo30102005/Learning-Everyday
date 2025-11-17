import mysql.connector
try:
  mydb = mysql.connector.connect(host='localhost', user='root', password='**********', database='db1')
  if mydb.is_connected():
    print('Connected to MySQL DataBase.')
    cursor = mydb.cursor()
    cursor.execute('show databases')
    for x in cursor:
      print(x)
  else:
    print('Not Connected to MySQL DataBase')  
except mysql.connector.Error as e:
  print("Error connecting MySQL", e)    
finally:
  if mydb.is_connected:
      cursor.close()