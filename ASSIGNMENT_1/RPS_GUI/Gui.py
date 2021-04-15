from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random as r
import os
import classRPS as cp 

moves={'Rock':'R','Paper':'P','Scissors':'S'}
computer={'R':'Rock','P':'Paper','S':'Scissors'}
#seed default-->current system time
r.seed()

def play_round(event):
    if but['text']=='RESET':
        rps.set_Num_Of_Rounds(7)
        but.config(text='PLAY')
        return
    if int(rps.roundcounter)==int(rps.rounds):
        but.configure(text='RESET')
        return
    #messagebox.showinfo('Information',message='Player Plays:'+str(combo.get())+'\nComputer Plays:'+str(computermove))
    text.config(state='normal')
    text.delete(0,'end')
    pen.config(state='normal')
    cen.config(state='normal')
    rps.round(moves[combo.get()])
    text.insert(0,computer[rps.computermove])
    text.config(state='readonly')
    if rps.win=='c':
        pen['fg']='green'
        cen['fg']='red'
    elif rps.win=='p':
        pen['fg']='red'
        cen['fg']='green'
    else:
        pen['fg']='black'
        cen['fg']='black'
    cen.delete(0,'end')
    pen.delete(0,'end')
    cen.insert(0,'Computer:'+str(rps.computerwins))
    pen.insert(0,'Player:'+str(rps.playerwins))
    cen.config(state='readonly')
    pen.config(state='readonly')


if __name__=='__main__':
    t=Tk()
    t.title('RPS GAME')
    t.geometry('400x400')
    f=Frame(t)
    rps=cp.rps()
    rps.set_Num_Of_Rounds(7)
    label=Label(f,text='Players Move',background='blue',foreground='white')
    label.grid(row=0,column=0,padx=10,pady=10)
    var=StringVar()
    combo=ttk.Combobox(f,width=15,textvariable=var)
    combo['values']=['Rock','Paper','Scissors']
    combo.grid(row=0,column=1,padx=10,pady=10)
    but=Button(f,text='Play',foreground='blue',background='white',font=16)
    but.bind('<Button>',play_round)
    but.grid(row=0,column=2,padx=10,pady=10)
    f.pack()
    f1=Frame(t)
    label1=Label(f1,text='Computer''s Move',background='blue',foreground='white')
    label1.grid(row=1,column=0,padx=10,pady=10)
    text=Entry(f1,width=15,font='21')
    text.config(state='readonly')
    text.grid(row=1,column=1,padx=10,pady=10)
    f1.pack()
    f2=Frame(t)
    f3=Frame(t)
    pen=Entry(f2,width=20)
    cen=Entry(f2,width=20)
    pen.insert(0,'Player:0')
    cen.insert(0,'Computer:0')
    pen.grid(row=2,column=0,padx=3,pady=5)
    pen.config(state='readonly')
    cen.grid(row=2,column=2,padx=3,pady=5)
    cen.config(state='readonly')  
    img=PhotoImage(file="./ICONS/RPS.png")
    img=img.subsample(1,1)
    label3=Label(f3,width=400,height=200,image=img)
    label3.grid(row=3,column=0,padx=10,pady=10)
    f2.pack()
    f3.pack()
    t.mainloop()
