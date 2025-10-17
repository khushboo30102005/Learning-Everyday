FILE_NAME = '08_File-Based-CRUD-App\cities.txt'

def read_all_records():
  try:
    with open(FILE_NAME, 'r') as file:
      records = [line.strip() for line in file if line.strip()]
    return records
  except FileNotFoundError:
    return []
  except:
    return []
  
def write_all_records(records):
  try:
    with open(FILE_NAME, 'w') as file:
      for record in records :
        file.write(record)
        file.write('\n')
  except:
    print("ERROR: Write Error")        

def create_record(new_record):
  try:
   with open(FILE_NAME, 'a') as file:
     file.write(new_record)
     file.write('\n')
  except:
    print('ERROR: Could not create record')

def display_record():
  records = read_all_records()
  if not records:
    print('\n---No Record Found---')
    return records
  print('\n----CURRENT RECORDS----')
  for index, record in enumerate(records):
    print(index+1, ' ', record)
  print('-------------------------')
  return records
  
def update_record(index, new_value):
  records = read_all_records()
  idx = index-1
  if 0<=idx<len(records):
    old_value = records[idx]
    records[idx] = new_value
    write_all_records(records)
    print('---RECORD UPDATED---')
  else:
    print('ERROR: Invalid record number')

def delete_record(index):
  records = read_all_records()
  idx = index-1
  if 0<=idx<len(records):
    delete_record = records.pop(idx)
    write_all_records(records)
  else:
    print('ERROR: Invalid record number')  

def main():
  while True:
    print("\n=====File CRUD Menu=====")
    print("1. Create new record (ADD RECORD)")
    print("2. Read all records (VIEW ALL)")
    print("3. Update record (UPDATE RECORD)")
    print("4. Delete a record (REMOVE)")
    print("5. EXIT")
    print("===========================")
    choice = int(input("Enter Your Choice (1-5):"))
    match(choice):
      case 1:
        new_item  = input("Enter city name:")
        if(new_item):
          create_record(new_item)
        else :
          print("WARNING: Record can't be empty")
      case 2:
        display_record()
      case 3:
        record = display_record()
        if record :
          try:
            record_num = int(input("enter record num to update:"))
            new_item = input("enter city name:")
            if(new_item):
              update_record(record_num, new_item)
            else :
              print("New City name can't be empty")
          except ValueError :
            print("ERROR: invalid input, please enter a number")    
      case 4:
            record = display_record()
            if record:
              try: 
                record_num = int(input("enter record number to delete:"))
                delete_record(record_num)
              except ValueError :
                print("ERROR: invalid input, please enter a number")  
      case 5:
        print("Thank You, GOODBYE!!")     
        break
      case _:
        print("ERROR: Invalid input, RETRY!!") 

if __name__=='__main__':
  main()      


