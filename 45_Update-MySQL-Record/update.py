import mysql.connector
class Employee:
  def __init__(self, data):
    self.id, self.Name, self.Manager_id = data
    
def updateEmployee(cursor, emp):
      q = "update employee set Name='{}', Manager_id={} where id={}".format(emp.Name, emp.Manager_id, emp.id)
      cursor.execute(q)

def main():
  try:
    mydb = mysql.connector.connect(host='localhost', user='root', password='***********', database='college')
    if mydb.is_connected():
      print('Database connect.')
      cursor = mydb.cursor()
      emp = Employee((101, 'Jhon Doe', 102))
      updateEmployee(cursor, emp)
      mydb.commit()
    else:
      print('Connection Failed.')  
             
  except mysql.connector.Error as e:
    print("Error: ", e)
  finally:
    if mydb.is_connected():
      mydb.close()
        
      
if __name__=='__main__':
  main()      
  
  
