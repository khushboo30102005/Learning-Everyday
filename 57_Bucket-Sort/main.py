import math

def insertion_sort(bucket):
  for i in range(1, len(bucket)):
    key = bucket[i]
    j = i-1
    while j>=0 and key<bucket[j]:
      bucket[j+1] = bucket[j]
      j-=1
    bucket[j+1] = key
  return bucket    

def bucket_sort(data_list):
  n = len(data_list)
  if n==0:
    return []
  min_value = min(data_list)  
  max_value = max(data_list) 
  range_size = (max_value-min_value+1)/n
  buckets = [[] for _ in range(n)]
  
  for item in data_list:
    index = math.floor((item - min_value)/range_size)
    index = min(n-1, index)
    buckets[index].append(item)

  for i in range(n):
    buckets[i] = insertion_sort(buckets[i])  
  k = 0
  for i in range(n):
    for j in range(len(buckets[i])):
      data_list[k] = buckets[i][j]
      k+=1
  return data_list
    
data = [64, 34, 25, 5, 22, 11, 90, 12]  
print("Before Sorted: ", data)
print("After Sorted: ",bucket_sort(data))