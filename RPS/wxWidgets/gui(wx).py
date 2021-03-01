import wx
import playground as pl


class Frame(wx.Frame):

    def panel1(self):
        panel=wx.Panel(self,wx.ID_ANY)
        gs=wx.GridSizer(0,3,3,3)
        self.st=wx.StaticText(panel,wx.ID_ANY,'Players Choice',wx.DefaultPosition,wx.Size(80,20))
        self.st.SetBackgroundColour(wx.Colour('#ffccff'))
        self.SetForegroundColour(wx.Colour('#000066'))
        self.choice=wx.ComboBox(panel,wx.ID_ANY,"",wx.DefaultPosition,wx.Size(50,20))
        self.butt=wx.Button(panel,wx.ID_ANY,'Play',wx.DefaultPosition,wx.Size(60,20))
        self.butt.Bind(wx.EVT_BUTTON,self.play,None)
        self.choice.Append('R')
        self.choice.Append('S')
        self.choice.Append('P')
        gs.Add(self.st)
        gs.Add(self.choice)
        gs.Add(self.butt)
        panel.SetSizer(gs)
        self.bx.Add(panel)

    def panel2(self):
       panel=wx.Panel(self,wx.ID_ANY)
       gs=wx.GridSizer(0,1,3,3)
       self.result=wx.TextCtrl(panel,wx.TEXT_ALIGNMENT_CENTER,'',wx.DefaultPosition,wx.Size(245,70),wx.TE_MULTILINE)
       gs.Add(self.result)
       panel.SetSizer(gs)
       self.bx.Add(panel)

    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'RPS GAME',wx.DefaultPosition,wx.Size(250,200))
        self.bx=wx.BoxSizer(wx.VERTICAL)
        self.panel1()
        self.panel2()
        self.SetSizer(self.bx)

    def play(self,event):
        g=pl.game()
        move=self.choice.GetValue()
        res=g.winner(move)
        self.result.SetValue(str(res))

class App(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show()
        return True

#MainLoop
a=App()
a.MainLoop()
