import tkinter as tk
from PIL import Image, ImageTk

def main():
  root=tk.Tk()
  root.geometry('400x400')
  
  # 1st image ==>
  image_path='./mysirg.png'
  pil_image=Image.open(image_path)
  tk_image=ImageTk.PhotoImage(pil_image)
  
  # 2nd image ==>   
  image_path2='./pillow-logo.png'
  pil_img2=Image.open(image_path2)
  pil_image=pil_image.resize((200,200))
  tk_img2=ImageTk.PhotoImage(pil_img2)
  
  l1=tk.Label(root, image=tk_image)
  l2=tk.Label(root,image=tk_img2)
  l1.pack(padx=10,pady=10)
  l2.pack(padx=10, pady=10)
  root.mainloop()
if __name__=='__main__':
  main()