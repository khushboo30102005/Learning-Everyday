""" l1 = [1,2,3,4,5]  
for ele in l1:
  print(ele) """    # output -> 1  2   3  4  5

""" x = 1234
for ele in x:
  print(ele) """    # Error : 'int' object is not iterable


class Counter:
  def __init__(self, start = 1, end = 10):
    self.start = start
    self.end = end
  def __iter__(self):
    return self.Counter_Iterator(self)  
  class Counter_Iterator:
    def __init__(self, counter):
      self.counter = counter
      self.beg = counter.start
    def __next__(self):
      if self.counter.start > self.counter.end:
        self.counter.start=self.beg
        raise StopIteration
      current_value = self.counter.start
      self.counter.start += 1
      return current_value
     
my_counter = Counter(1,5)    

for i in my_counter:
  print(i)
print('*****************')

my_counter = Counter(6,10)  
for i in my_counter:
  print(i)
print('*****************')

my_counter = Counter(11,20)  
for i in my_counter:
  print(i)
print('*****************')
