import subprocess
print('Enter Three Numbers:')
a,b,c = input(), input(), input(0)
subprocess.run(['./c_code',a,b,c])
