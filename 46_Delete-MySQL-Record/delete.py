import mysql.connector
class Employee:
  def __init__(self, data):
    self.id, self.Name, self.Manager_id = data
 
def deleteEmployee(cursor, emp):
  q="DELETE FROM employee WHERE id={}".format(emp.id)   
  cursor.execute(q) 
  print('Record has been deleted...')


def main():
  try:
    mydb = mysql.connector.connect(host='localhost', user='root', password='*********', database='college')
    if mydb.is_connected():
      print('Database connect.')
      cursor = mydb.cursor()
      emp = Employee((101, 'Jhon Doe', 102))
      deleteEmployee(cursor, emp)
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
  
  
