# GENERATORS ==>
""" def fun():
  yield 10 
  yield 20 
  yield 30 
 
it = fun()

for x in it:
  print(x) """
# Write a generator method to produces n prime numbers ==>
def isPrime(n):
  for i in range(2,n):
    if n%i==0:
      return False
    return True
def nextPrime(n):
  while not isPrime(n:=n+1):
    pass
  return n  
def primeGenerator(n):
  x = 2
  while n:
    if isPrime(x):
      n-=1
      yield x
    x=nextPrime(x)  

prime_list=[num for num in primeGenerator(100)]  
print(prime_list)

