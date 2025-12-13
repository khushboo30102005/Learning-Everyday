a = 10
print(a)
del a   # delete  reference variable a only that is created in NameSpace 
# print(a) # Error ==> NameError: name 'a' is not defined
# del keyword can't delete real object that is exist in PHS (Private Heap Space)