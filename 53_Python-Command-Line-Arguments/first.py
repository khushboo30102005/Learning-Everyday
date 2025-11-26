import sys
def avg():
  l = [int(e) for e in sys.argv[1::]]
  print(sum(l)/len(l))
  
avg()  