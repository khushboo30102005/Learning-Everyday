# def f1(a):  # a is get address/ id of int obj 
#   print(id(a))
#   a += 1
#   print(id(a))  # here,  new Obj created 
#   print(a)
   
# b = 5    # b contain address/ id of int obj 
# print(id(b))  # parameter passing => object reference
# f1(b)   
# print(b)

def f1(a):
  print(id(a))
  a[0] = 99
  print(id(a))  # here,  new Obj created 
  print(a)
   
b = [2,4,6,7,9]  # lists are mutable
print(b)
print(id(b))  # parameter passing => object reference
f1(b)   
print(b)