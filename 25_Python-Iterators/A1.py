l1 = [10,20,30,40,50,60]
# print(l1[0])

# for x in l1:
#   print(x)

it=iter(l1)

while True:
  try:
    x=next(it)
    print(x)
  except StopIteration:
    break

print('Done')
