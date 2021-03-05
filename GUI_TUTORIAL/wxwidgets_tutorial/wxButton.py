import wx
import random as r


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'Button Example',wx.DefaultPosition,wx.Size(200,200))
        self.bx=wx.BoxSizer(wx.VERTICAL)
        self.but=wx.Button(self,wx.ID_ANY,'CREATE',wx.DefaultPosition,wx.Size(60,20),)
        self.Bind(wx.EVT_BUTTON,self.create,None)
        self.bx.Add(self.but)
        self.SetSizer(self.bx)
    def create(self,event):
        wx.MessageBox('Random Number Generated:'+str(r.randint(1000,10000)))

class app(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show(True)
        return True

a=app()
a.MainLoop()