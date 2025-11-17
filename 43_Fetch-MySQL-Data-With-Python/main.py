import mysql.connector
def fetchEmployee(cursor):
  cursor.execute('select * from employee')
  return list(cursor)
def main():
  try:
    mydb = mysql.connector.connect(host='localhost', user='root', password='********', database='college')
    if mydb.is_connected():
      print('MySQL database connected')
      cursor = mydb.cursor()
      empList = fetchEmployee(cursor)
      for record in empList:
        print(record)
    else:
      print('MySQL database is not connected')  
  except mysql.connector.Error as e:
    print("Error: ",e)
  finally:
    if mydb.is_connected():
      cursor.close()
  
if __name__=='__main__':
  main()  