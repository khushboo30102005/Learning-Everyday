import tkinter as tk
from tkinter import ttk
def convert_length(value, unit):
  if unit=='feet':
    meters=value*0.3048
  elif unit=='inches':
    meters=value*0.0254
  elif unit=='meters':
    meters=value
  elif unit=='centimeter':
    meters=value/100
  result = {
    'meters': meters,
    'centimeter':meters*100,
    'feet': meters/0.3048,
    'inches':meters/0.0254
  }  
  return result
def convert(t1, selected_unit, l1):
   result = convert_length(float(t1.get()),selected_unit.get())
   msg=str(result['meters']) + ' meters\n'
   msg=msg+str(result['centimeter']) +' centimeter\n'
   msg=msg+str(result['feet']) +' feet\n'
   msg=msg+str(result['inches']) +' inches\n'
   l1.config(text=msg)
def  main():
  root = tk.Tk()
  root.title('Unit Converter')
  root.geometry("400x400")
  root.config(bg="#f0f4f7")
  t1=ttk.Entry(root, width=20, font=('Arial', 20))
  units=['meters', 'centimeter', 'feet', 'inches']
  selected_unit=tk.StringVar()
  cb1=ttk.Combobox(root, textvariable=selected_unit, values=units, font=('Arial', 20))
  cb1.set(units[0])
  l1=ttk.Label(root, text="", font=('Arial', 20))
  b1=ttk.Button(root, text='convert', command=lambda:convert(t1, selected_unit, l1))
  t1.pack(padx=10, pady=10)
  cb1.pack(padx=10, pady=10)
  b1.pack(padx=10, pady=10)
  l1.pack(padx=10, pady=10)
  root.mainloop()
  
if __name__=='__main__':
  main()  