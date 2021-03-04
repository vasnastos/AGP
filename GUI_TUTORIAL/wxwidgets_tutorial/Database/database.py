import wx
import re
import wx.adv
import sqlite3 as sq

class database:
    def __init__(self):
       self.conn=sq.connect('Database/test.db')
       self.db=self.conn.cursor()
    def destroy(self):
        self.conn.close()
    def data(self):
        data=''
        sql='select * from car'
        for x in self.db.execute(sql):
             data+=str(x[0])+','+str(x[1])+','+str(x[2])+'\n'
        return data
    def insert(self,m,b,p):
       sql='insert into car(model,brand,price) values(?,?,?)'
       self.db.execute(sql,(m,b,p))
       self.conn.commit()
    
    def csv_Extract(self):
        sql='select *from car'
        data='Model;Brand;Price\n'
        for x in self.db.execute(sql):
             data+=str(x[0])+';'+str(x[1])+';'+str(x[2])+'\n'
        return data

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'Database Demo',wx.DefaultPosition,wx.Size(500,500))
        self.bx=wx.BoxSizer(wx.VERTICAL)
        anim=wx.adv.Animation('Database/database.gif')
        animctrl=wx.adv.AnimationCtrl(self,wx.ID_ANY,anim,wx.DefaultPosition,wx.Size(490,250))
        animctrl.Play()
        self.sdb=database()
        self.bx.Add(animctrl)
        panel=wx.Panel(self,wx.ID_ANY)
        gs=wx.GridSizer(0,3,20)
        self.but1=wx.Button(panel,wx.ID_ANY,'EXTRACT',wx.DefaultPosition,wx.Size(80,20))
        self.but2=wx.Button(panel,wx.ID_ANY,'INSERT',wx.DefaultPosition,wx.Size(80,20))
        self.but3=wx.Button(panel,wx.ID_ANY,'SAVE',wx.DefaultPosition,wx.Size(80,20))
        self.but1.Bind(wx.EVT_BUTTON,self.extract,None)
        self.but2.Bind(wx.EVT_BUTTON,self.insert,None)
        self.but3.Bind(wx.EVT_BUTTON,self.save,None)
        gs.Add(self.but1)
        gs.Add(self.but2)
        gs.Add(self.but3)
        panel.SetSizer(gs)
        self.bx.AddSpacer(5)
        self.bx.Add(panel)
        self.SetSizer(self.bx)
    def destroy(self):
        self.mydb.destroy()

    def extract(self,event):
         wx.MessageBox(self.sdb.data())
    def insert(self,event):
        dial=wx.TextEntryDialog(self,'Give Car model')
        if dial.ShowModal()==wx.ID_CANCEL:
            return
        model=dial.GetValue()
        dial=wx.TextEntryDialog(self,'Give Car Brand')
        if dial.ShowModal()==wx.ID_CANCEL:
            return
        brand=dial.GetValue()
        dial=wx.TextEntryDialog(self,'Give Car price')
        if dial.ShowModal()==wx.ID_CANCEL:
            return
        price=dial.GetValue()
        if re.match('[0-9][0-9]*\.?[0-9]*',price):
            print('Price Accepted By  interpenter')
            self.sdb.insert(model,brand,price)
        else:
            wx.MessageBox('Unacceptable price:'+str(price))
    def save(self,event):
        dial=wx.FileDialog(self,'Open file','.','','',wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if dial.ShowModal()==wx.ID_CANCEL:
            wx.MessageBox('you did not select a file')
            return
        filename=dial.GetPath()
        y=open(filename,'w')
        y.write(self.sdb.csv_Extract())
        y.close()
        print('File Successfuly saved:'+str(filename))

class app(wx.App):
    def OnInit(self):
        self.f=Frame()
        self.f.Show()
        return True
    def destroy(self):
        self.f.destroy()

a=app()
a.MainLoop()
a.destroy()
