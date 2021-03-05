from wx import *
import sys

class menu:
    OPEN=100
    SAVE=101
    EXPORT=102
    CLOSE=103


class frame(Frame):
    def make_menu(self):
        men=Menu()
        bar=MenuBar()
        men.Append(menu.OPEN,'OPEN')
        men.Append(menu.SAVE,'SAVE')
        men.Append(menu.EXPORT,'EXPORT')
        men.Append(menu.CLOSE,'CLOSE')
        self.Bind(EVT_MENU,self.open,None,menu.OPEN)
        self.Bind(EVT_MENU,self.exit,None,menu.CLOSE)
        self.Bind(EVT_MENU,self.export,None,menu.EXPORT)
        self.Bind(EVT_MENU,self.save,None,menu.SAVE)
        bar.Append(men,'OPTIONS')
        self.SetMenuBar(bar)
    def __init__(self):
        Frame.__init__(self,None,ID_ANY,'Menu Demo',DefaultPosition,Size(250,250))
        self.bx=BoxSizer()
        self.make_menu()
        self.out=TextCtrl(self,ID_ANY,'',DefaultPosition,Size(200,120))
        self.bx.Add(self.out)
        self.SetSizer(self.bx)
    
    def open(self,event):
       self.out.SetValue('Open Menu Option Selected')
    def exit(self,event):
       sys.exit(0)
    def export(self,event):
       self.out.SetValue('export menu option selected')
    def save(self,event):
       self.out.SetValue('Save menu option selected')


class app(App):
    def OnInit(self):
        f=frame()
        f.Show()
        return True

a=app()
a.MainLoop()