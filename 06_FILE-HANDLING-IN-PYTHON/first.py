import os
def write_to_file(filename, name):
  # f = open(filename,'w')
  # f.write(name)
  # f.close()
  with open(filename, 'w') as f :
    f.write(name)

def append_to_file(filename, name):
  f = open(filename,'a')
  f.write('\n')
  f.write(name)
  f.close()

def read_from_file(filename):
  f = open(filename,'r')
  text = f.read()
  print(text)  

def main():
  name = input("enter your name:")
  write_to_file('file1.txt', name)
  # append_to_file('file1.txt', name)
  # read_from_file('file1.txt')
  # os.rename('file1.txt', 'name.txt')
  # os.remove('name.txt')
main()