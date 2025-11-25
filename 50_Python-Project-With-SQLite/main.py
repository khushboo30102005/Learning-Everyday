import sqlite3
DATABASE_NAME = 'book_records.db'

def connect_to_sqlite():
  try:
    con = sqlite3.connect("DATABASE_NAME")
    print("DtaBase Connection Establish")
  except:
    print("Some Error")  
  return con  

def create_table(con):
  q = "CREATE TABLE IF NOT EXISTS book("\
    "bookID INTEGER PRIMARY KEY, "\
      "title TEXT NOT NULL, "\
        "price REAL NOT NULL, "\
          "author TEXT NOT NULL);"
  cursor = con.cursor()     
  cursor.execute(q)   

def insert_record(con, my_books):
  cursor = con.cursor()
  q = "INSERT INTO book (bookID, title, price, author) VALUES (?, ?, ?, ?)"
  cursor.executemany(q, my_books)
  print(len(my_books), 'records inserted')
  con.commit()

def view_record(con):
  q = "SELECT * FROM book"
  cursor = con.cursor() 
  cursor.execute(q)
  rows = cursor.fetchall()
  for row in rows:
    print(row)
def main():
  con = connect_to_sqlite()
  create_table(con)
  my_books = [
    (1, "Java", 500, "SS"),
    (2, "JavaScript", 540, "SP"),
    (3, "Python", 200, "AS"),
    (4, "AI/ML", 970, "KS"),
    (5, "Data Science", 830, "KK"),
    (6, "DBMS", 500, "AS"),
  ]
  insert_record(con, my_books)
  view_record(con)
  if con:
    con.close()

if __name__=='__main__':
  main()
  