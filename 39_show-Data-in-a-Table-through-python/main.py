import tkinter as tk
from tkinter import ttk
data_cols = ["Item ID", "Product Name", "Price(INR)", "Stock"]

sample_data = [
  (101, "Wireless Mouse", 850, 45),
  (102, "Mechanical Keyboard", 4200, 15),
  (103, "USB-C Hub", 1500, 70),
  (104, "Laptop Stand", 990, 55),
  (105, "Monitor cable", 450, 120),
]

def create_table_gui():
  root=tk.Tk()
  root.title("Data Table Using Treeview")
  root.geometry("800x300")
  tree = ttk.Treeview(root, columns=data_cols, show='headings', height=10)
  for col in data_cols:
    tree.column(col, anchor=tk.CENTER, width=120)
    tree.heading(col, text=col)
    
  for item in sample_data:
    tree.insert('', tk.END, values=item)
  
  tree.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)    
  root.mainloop()
if __name__=='__main__':
  create_table_gui()