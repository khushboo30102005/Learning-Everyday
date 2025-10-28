import xml.etree.ElementTree as ET

tree=ET.parse('employee.xml')
root=tree.getroot()
# print(root)
print("Name  | Gender  |  Age  | Email   |  Phone  |  Address")
for emp in root.findall('employee'):
  name=emp.find('name').text
  gender=emp.find('gender').text
  age=emp.find('age').text
  email=emp.find('email').text
  phone=emp.find('phone').text
  address=emp.find('address').text
  print('{} | {} | {} | {} | {} | {}'.format(name, gender, age, email, phone, address))