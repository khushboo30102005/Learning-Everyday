import xml.etree.ElementTree as ET

tree=ET.parse('employee.xml')
root=tree.getroot()
# print(root)

# display Data ==>

print("Name  | Gender  |  Age  | Email   |  Phone  |  Address")
for emp in root.findall('employee'):
  name=emp.find('name').text
  gender=emp.find('gender').text
  age=emp.find('age').text
  email=emp.find('email').text
  phone=emp.find('phone').text
  address=emp.find('address').text
  print('{} | {} | {} | {} | {} | {}'.format(name, gender, age, email, phone, address))

# Update existing data  ==>

for emp in root.findall('employee'):
  name=emp.find('name').text
  if name == 'Rahul':
   emp.find('age').text = '30'
    

   


# Add a new Employee ==> 

new_employee=ET.SubElement(root,'employee')
ET.SubElement(new_employee, 'name').text='kiran'
ET.SubElement(new_employee, 'gender').text= 'Female'
ET.SubElement(new_employee, 'age').text= '21'
ET.SubElement(new_employee, 'email').text= 'kiran@gmial.com'
ET.SubElement(new_employee, 'phone').text= '1234567890'
ET.SubElement(new_employee, 'address').text= 'xyz'

# Remove a Employee ==>

for emp in root.findall('employee'):
  name=emp.find('name').text
  if name == 'Rahul':
    root.remove(emp)


# Save changes back to the file
tree.write('employee.xml') 