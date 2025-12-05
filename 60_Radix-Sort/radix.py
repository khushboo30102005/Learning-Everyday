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


def radix_sort(arr):
    if not arr: 
      return arr
    maxValue = max(arr)
    print(maxValue)
    exp = 1
    while maxValue // exp > 0:
      print("\nPass for digit position (exp:{})".format(exp))
      counting_sort(arr, exp)
      print("List after pass: ", arr)
      exp *= 10
    return arr
    
    
if __name__ == "__main__":
    data = [820, 81, 92, 43, 155, 35, 76, 517]  
    print("Original Array: ", data)
    sorted_data = radix_sort(data)
    print("Sorted Array: ", sorted_data)

 
