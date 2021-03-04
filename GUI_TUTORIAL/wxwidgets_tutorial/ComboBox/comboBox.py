import wx 
import os


filepath=os.getcwd()+'/'

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'ComboBox Example',wx.DefaultPosition,wx.Size(350,300))
        self.bx=wx.BoxSizer(wx.VERTICAL)
        panel=wx.Panel(self,wx.ID_ANY)
        self.cmb=wx.ComboBox(panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(100,20))
        list=['file1.txt','file2.txt','file3.csv']
        self.cmb.AppendItems(list)
        self.cmb.Bind(wx.EVT_COMBOBOX,self.comboSlot,None)
        self.area=wx.TextCtrl(panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(210,220),wx.TE_MULTILINE)
        gs=wx.GridSizer(0,2,5)
        gs.Add(self.cmb)
        gs.Add(self.area)
        panel.SetSizer(gs)
        self.bx.Add(panel)
        self.SetSizer(self.bx)

    def comboSlot(self,event):
        self.area.Clear()
        filename=filepath+'ComboBox/'+str(self.cmb.GetValue())
        y=open(filename,'r')
        msg=''
        for x in y:
            msg+=x+'\n'
        y.close()
        self.area.SetValue(msg)


class app(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show()
        return True

a=app()
a.MainLoop()