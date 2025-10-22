def printN(n):
  if(n == 1):
    print(1)
  elif(n>1):
    printN(n-1)
    print(n)

printN(5)    