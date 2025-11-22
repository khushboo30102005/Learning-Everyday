import time
def isPrime(num):
  if num <= 1:
    return False
  for i in range(2,num):
    if num%i ==  0:
      return False
  return True
    
  
  
def isOptimizedPrime(num):
  if num<=1:
    return False
  if num<=3:
    return True
  if num%2==0 or num%3==0:
    return False
  i=5
  while i*i<=num :
    if num%i==0 or num%(i+2)==0:
      return False
    i+=6
  return True  


num = int(input("Enter a number: "))

# ---- Brute Force ----
print("\nBrute Force Solution:")
start = time.time()
res = isPrime(num)
end = time.time()
print("Time:", "%.6f sec" % (end - start))
print("Result:", "Prime" if res else "Not Prime")

# ---- Optimized ----
print("\nOptimized Solution:")
start = time.time()
resOpt = isOptimizedPrime(num)
end = time.time()
print("Time:", "%.6f sec" % (end - start))
print("Result:", "Prime" if resOpt else "Not Prime")