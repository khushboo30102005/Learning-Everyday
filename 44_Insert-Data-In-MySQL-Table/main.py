import mysql.connector
class Employee:
  def __init__(self, data):
    self.id, self.Name, self.Manager_id = data

def insertEmployee(cursor, emp):
  q= 'insert into employee (id, Name, Manager_id ) values ({}, "{}", {})' .format(emp.id, emp.Name, emp.Manager_id )   
  cursor.execute(q)
def fetchEmployee(cursor):
  cursor.execute('select * from employee')
  return list(cursor)
def main():
  try:
    mydb = mysql.connector.connect(host='localhost', user='root', password='********', database='college')
    if mydb.is_connected():
      print("MySQL is Connected")
      cursor = mydb.cursor() 
      emp=Employee((105, 'johnsmith', 102))
      insertEmployee(cursor, emp)
      mydb.commit()
      emp = fetchEmployee(cursor)
      for record in emp:
        print(record)
    else :
      print('Connection failed')      
  except mysql.connector.Error as e:
    print("Error: ", e)
  finally:
    if mydb.is_connected():
      mydb.close()
      

if __name__=='__main__':
  main()      