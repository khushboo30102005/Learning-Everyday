import tkinter as tk
def setTextColor(l1, color):
  l1.config(fg=color)
def main():
  root=tk.Tk()
  root.geometry("400x400")
  l1=tk.Label(root, text="Change Color", font=('Arial',20,"bold"))
  b1=tk.Button(root, text="RED",bg='red',fg='white', command=lambda: setTextColor(l1, 'red'))
  b2=tk.Button(root, text="BLUE",bg='blue', fg='white', command=lambda: setTextColor(l1, 'blue'))
  b3=tk.Button(root, text="GREEN",bg='green',fg='white',  command=lambda: setTextColor(l1, 'green'))

  l1.pack(padx=10, pady=10)
  b1.pack(padx=10, pady=10)
  b2.pack(padx=10, pady=10)
  b3.pack(padx=10, pady=10)
  root.mainloop()

if __name__=='__main__':
  main()
