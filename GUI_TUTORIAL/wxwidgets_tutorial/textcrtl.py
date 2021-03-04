import wx

class Frame(wx.Frame):
    def panel1(self):
        panel=wx.Panel(self,wx.ID_ANY)
        gs=wx.GridSizer(0,2,10)
        self.edit=wx.TextCtrl(panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(60,20))
        self.but=wx.Button(panel,wx.ID_ANY,'ADD TEXT',wx.DefaultPosition,wx.Size(100,20))
        self.but.SetForegroundColour(wx.Colour('#6e2d55'))
        self.but.SetBackgroundColour(wx.Colour('#1aba7f'))
        self.but.Bind(wx.EVT_BUTTON,self.update,None)
        gs.Add(self.edit)
        gs.Add(self.but)
        panel.SetSizer(gs)
        self.bx.Add(panel)

    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'TEXTCTRL DEMO',wx.DefaultPosition,wx.Size(200,200))
        self.bx=wx.BoxSizer(wx.VERTICAL)
        self.panel1()
        self.output=wx.TextCtrl(self,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(200,100),wx.TE_MULTILINE)
        self.bx.Add(self.output)
        self.SetSizer(self.bx)
    def update(self,event):
        text=self.edit.GetValue()
        previous=self.output.GetValue()
        self.output.SetValue(previous+'\n'+text)


class App(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show()
        return True

a=App()
a.MainLoop()