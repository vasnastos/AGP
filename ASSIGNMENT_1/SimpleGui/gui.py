import tkinter as tk
import rps 
from tkinter import ttk,messagebox


moves={'Rock':'R','Paper':'P','Scissors':'S'}
outcome={'p':'Player','c':'Computer','t':'Tie Game'}


def play():
    #Ελέγχω αν ο αριθμός των γύρων είναι 0.
    if int(rpsobject.rounds)==0:
        messagebox.showerror('Error in Rounds','Please Insert Number of Rounds')
        return
    playermove=player.get()
    if int(rpsobject.roundcounter)==int(rpsobject.rounds):
        resultBox.config(text=str(rpsobject))
        return
    rpsobject.round(moves[playermove])
    #Εμφανίζω στο παράθυρο την κίνηση του υπολογιστή
    comp.config(state='normal')
    comp.delete(0,'end')
    comp.insert(0,rpsobject.ComputerMove())
    #comp.insert(2,'This is a Test')
    comp.config(state='readonly')
    resultBox.config(text='Winner:'+str(outcome[rpsobject.win]))
 
def setRounds():
    #Εισαγωγή αριθμού γύρων παιχνιδιού
    if len(rnds.get())==0:
        messagebox.showerror('Unfill blank','You do not insert a number--Please insert a number')
        return
    rpsobject.set_Num_Of_Rounds(int(rnds.get()))

#Main Window
root=tk.Tk()
rpsobject=rps.rps()
root.title('Rps Game')
root.geometry('550x330')

#First Frame
frame=tk.Frame(master=root)
label=tk.Label(master=frame,width=10,justify=tk.CENTER,bg='gray',fg='blue',bd=5,text='Player\'s Move')
player=ttk.Combobox(master=frame,width=10,justify=tk.CENTER,values=('Rock','Paper','Scissors'))
playbutton=tk.Button(master=frame,width=20,bg='blue',fg='white',bd=3,text='Play',command=play)
label.grid(row=0,column=0,padx=10,pady=10)
player.grid(row=0,column=1,padx=10,pady=10)
playbutton.grid(row=0,column=2,padx=10,pady=10)
frame.pack()

#Second Frame
frame2=tk.Frame(master=root)
lb=tk.Label(master=frame2,width=25,justify=tk.CENTER,bg='gray',fg='blue',bd=5,text='Computer\'s move')
comp=tk.Entry(master=frame2,width=25,justify=tk.CENTER,fg='blue',bd=5,state='readonly')
lb.grid(row=1,column=0,padx=14,pady=10)
comp.grid(row=1,column=1,padx=14,pady=10)
frame2.pack()

#Third Frame
frame3=tk.Frame(master=root)
lab=tk.Label(master=frame3,width=19,justify=tk.CENTER,bg='gray',fg='blue',bd=5,text='Number of Rounds')
rnds=tk.Entry(master=frame3,width=12,justify=tk.CENTER,fg='blue',bd=5)
roundButton=tk.Button(master=frame3,width=20,bg='blue',fg='white',bd=3,text='Rounds',command=setRounds)
lab.grid(row=3,column=0,padx=7,pady=10)
rnds.grid(row=3,column=1,padx=7,pady=10)
roundButton.grid(row=3,column=2,padx=7,pady=10)
frame3.pack()

textheight=int(0.5*root.winfo_screenheight())
resultBox=tk.Label(master=root,font=("calibri",23),width=30,height=textheight,justify=tk.CENTER,fg='red',text='Outcome')
resultBox.pack()


#Mainloop and Window Destroy
tk.mainloop()
root.destroy()


