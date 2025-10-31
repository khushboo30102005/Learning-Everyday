class Integer:
  def __init__(self, data):
    self.data = data
  def __iter__(self):
    return self.Integer_Iterator(self)  
  class Integer_Iterator:
    def __init__(self, integer):
      self.integer = integer
      self.separate_digits()
      self.i = 0
    def separate_digits(self):
      value=self.integer.data 
      l1 = [int(e)  for e in str(value)]   
      self.myList = l1
    def __next__(self):
      if self.i == len(self.myList):
        raise StopIteration
      current_value = self.myList[self.i]
      self.i += 1
      return current_value


num = 1234
x = Integer(num)
for ele in x:
  print(ele) 
print(num)  
print('***************')
num = 1234
x = Integer(num)
for ele in x:
  print(ele) 
print(num)  
print('***************')