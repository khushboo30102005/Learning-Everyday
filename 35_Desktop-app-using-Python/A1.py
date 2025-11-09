import tkinter as tk
root=tk.Tk()
def greeting(l2,t1):
  name=t1.get()
  msg='Hello '+name+', How are you?'
  l2.config(text=msg)

root.title('My First GUI Application')
root.geometry("600x400")
l1=tk.Label(root, text="Enter Your Name: ")
# l1.pack()
l1.grid(row=0,column=0)
t1=tk.Entry(root,width=50)
# t1.pack()
t1.grid(row=0,column=1)
l2=tk.Label(root, text='',  # foreground="white",  Set the text color to white
     font=("Arial",14))
l2.grid(row=2,column=1)
b1=tk.Button(root, text="Enter",command=lambda:greeting(l2,t1))
b1.grid(row=1,column=1)
root.mainloop()