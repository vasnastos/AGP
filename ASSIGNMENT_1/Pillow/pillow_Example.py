import tkinter as tk
from PIL import ImageTk,Image
#PIL
#Pillow Python Imaging Library
#pip install pillow


Root=tk.Tk()
Root.title('Image Loader')
Root.geometry("550x300")
Root.resizable(width=False,height=True)
w=tk.Canvas(master=Root,bd=2,width=Root.winfo_screenwidth(),height=Root.winfo_screenheight())
imgfirst=Image.open("Rps.png")
print(Root.winfo_screenwidth(),Root.winfo_screenheight())
subsampleimage=imgfirst.resize((500,250),Image.ANTIALIAS)
w.pack()
img=ImageTk.PhotoImage(subsampleimage)
w.create_image((250,150),image=img)
tk.mainloop()