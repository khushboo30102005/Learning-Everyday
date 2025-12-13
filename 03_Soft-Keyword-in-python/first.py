import keyword as kw

keyWords = kw.kwlist
print(len(keyWords))   #35

""" 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

softKeywords = kw.softkwlist
print(softKeywords)

""" 
['_', 'case', 'match', 'type']
"""

def f1(x):
  return x

action = f1('Hekllo')
  
match action:
  case 10:
    print('10 is my Lucky Number')
  case 'Hello':
    print('Hello Python...')  
  case '1+4j':
    print('This is a complex Number.') 
  case _:
    print('Here WE Discus SoftKeyWords.')  
    
type point = tuple[float, float] 
type list_of_points = list[point]   
p1:point = (3.4, 7.5)
p2:point = (2.5, 6.1)
p3:point = (1.4, 3.5)
my_list:list_of_points = [p1, p2, p3]
print(my_list)