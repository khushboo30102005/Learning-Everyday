from ctypes import *;
c_file_path = 'C:/Users/T14/Desktop/MySirG-100days-learning-challenge/31_Call-Code_From-Python/customlib1.dll'
c_fun = CDLL(c_file_path)
a = c_fun.lcm(4,6)
b= c_fun.isPrime(11)
c= c_fun.fact(5)
print(a,b,c)