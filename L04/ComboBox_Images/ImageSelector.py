from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk


def select(event):
    image=combo.get()
    print(f'Image Selected:{image}')
    img=Image.open(str(image))
    subsampleimage=img.resize((500,250),Image.ANTIALIAS)
    selected=ImageTk.PhotoImage(subsampleimage)
    label.configure(image=selected)
    label.image=selected
   

root=tk.Tk()
root.geometry('550x330')
root.title('Image Selected by ComboBox')
combo=ttk.Combobox(master=root,width=50,values=('Rock.png','paper.png','scissors.png'))
combo.bind('<<ComboboxSelected>>',select)
combo.pack()
labelheight=int(root.winfo_screenheight()*0.7)
label=tk.Label(master=root,width=root.winfo_screenwidth(),height=labelheight,bd=5)
label.pack()
tk.mainloop()
