import random
import time

def is_sorted(data):
  for i in range(len(data) - 1):
    if data[i] > data[i+1]:
      return False
  return True

def bogo_sort(data):
  print("---Starting Bogo sort (May Take Time!!)---")
  attempts = 0
  start_time = time.time()
  while not is_sorted(data):
    random.shuffle(data)
    attempts += 1
    if attempts > 10000000:
      print("Reached max attempts.")
      break
    
  end_time = time.time()  
  t = end_time - start_time
  if is_sorted(data):
    print("{} attempts in %0.4f seconds".format(attempts)%t)
  return data

if __name__== "__main__":
  list_bogo = [3, 1, 10, 4, 8, 2, 9, 7, 6, 5]
  print("Original List: ", list_bogo)
  sorted_list = bogo_sort(list_bogo)
  print("Original List: ", sorted_list)
    