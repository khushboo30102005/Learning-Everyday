def counting_sort(arr, exp):
  
  n = len(arr)
  output = [0] * n
  count = [0] * 10
  
  for i in range(n):
    index = arr[i] // exp
    digit = index % 10
    count[digit] += 1
    
  for i in range(1, 10):
    count[i] += count[i-1]
    
  i = n-1
  while i >= 0:
    index = arr[i] // exp
    digit = index % 10
    output[count[digit]-1] = arr[i]
    count[digit] -= 1
    i -= 1
    
  for i in range(n):
    arr[i] = output[i]  
    
    
data = [55, 20, 81, 76, 92, 43, 35, 17]   
 
counting_sort(data, 10)
print(data)