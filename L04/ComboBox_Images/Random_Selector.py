from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from time import time
import random as r


r.seed(time()*1000)
images={1:'Rock.png',2:'paper.png',3:'scissors.png'}

def generate():
    pos=r.randint(1,3)
    print(f'Image Selected:{images[pos]}')
    img=Image.open(str(images[pos]))
    subsampleimage=img.resize((500,250),Image.ANTIALIAS)
    selected=ImageTk.PhotoImage(subsampleimage)
    label.configure(image=selected)
    label.image=selected
    #label['image']=selected
   

root=tk.Tk()
root.geometry('550x330')
root.title('Image Selected by ComboBox')
but=tk.Button(master=root,width=25,fg='blue',bg='gray',text='IMAGE',command=generate)
but.pack()
labelheight=int(root.winfo_screenheight()*0.7)
label=tk.Label(master=root,width=root.winfo_screenwidth(),height=labelheight,bd=5)
label.pack()
tk.mainloop()
