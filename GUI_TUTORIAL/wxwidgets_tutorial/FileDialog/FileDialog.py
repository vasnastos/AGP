import wx
import logging as l
import os

filename=os.getcwd()+'\\FileDialog'
print(filename)

class Frame(wx.Frame):
    def buttonsstyle(self):
        self.but1.SetForegroundColour(wx.Colour('#4a253e'))
        self.but1.SetBackgroundColour(wx.Colour('#abbec9'))
        self.but2.SetForegroundColour(wx.Colour('#4a253e'))
        self.but2.SetBackgroundColour(wx.Colour('#abbec9'))
        self.but3.SetForegroundColour(wx.Colour('#4a253e'))
        self.but3.SetBackgroundColour(wx.Colour('#abbec9'))
        self.but4.SetForegroundColour(wx.Colour('#4a253e'))
        self.but4.SetBackgroundColour(wx.Colour('#abbec9'))

    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'FILEDIALOG',wx.DefaultPosition,wx.Size(500,360))
        self.bx=wx.BoxSizer(wx.VERTICAL)
        self.but1=wx.Button(self,wx.ID_ANY,'LOAD',wx.DefaultPosition,wx.Size(480,20))
        self.but2=wx.Button(self,wx.ID_ANY,'SAVE',wx.DefaultPosition,wx.Size(480,20))
        self.but3=wx.Button(self,wx.ID_ANY,'LOAD LOCAL',wx.DefaultPosition,wx.Size(480,20))
        self.but4=wx.Button(self,wx.ID_ANY,'SAVE LOCAL',wx.DefaultPosition,wx.Size(480,20))
        self.output=wx.TextCtrl(self,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(480,200),wx.TE_MULTILINE)
        self.buttonsstyle()
        self.but1.Bind(wx.EVT_BUTTON,self.opend,None)
        self.but2.Bind(wx.EVT_BUTTON,self.saved,None)
        self.but3.Bind(wx.EVT_BUTTON,self.openl,None)
        self.but4.Bind(wx.EVT_BUTTON,self.savel,None)
        self.bx.Add(self.output)
        self.bx.AddSpacer(5)
        self.bx.Add(self.but1)
        self.bx.AddSpacer(5)
        self.bx.Add(self.but2)
        self.bx.AddSpacer(5)
        self.bx.Add(self.but3)
        self.bx.AddSpacer(5)
        self.bx.Add(self.but4)
        self.SetSizer(self.bx)
    def opend(self,event):
        dial=wx.FileDialog(self,'Open File','.',"","",wx.FD_OPEN)
        if dial.ShowModal()==wx.ID_CANCEL:
            wx.MessageBox('You did not select a file')
            return
        filepath=dial.GetPath()
        y=open(filepath,'r')
        msg=''
        for x in y:
            msg+=x+'\n'
        y.close()
        self.output.SetValue(msg)
        print(msg)
    
    def saved(self,event):
        outputText=self.output.GetValue()
        if len(outputText)==0:
            wx.MessageBox('You did not have anything to Store')
            return
        dial=wx.FileDialog(self,'Save File','.','','',wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if dial.ShowModal()==wx.ID_CANCEL:
            wx.MessageBox('you did not select a file')
            l.error('No file selected!!!!')
            return
        filename=dial.GetPath()
        y=open(filename,'w')
        y.write(outputText)
        y.close()

    def openl(self,event):
        filen=filename+'\\local.txt'
        y=open(filen)
        msg=''
        for x in y:
           msg+=x+'\n'
        self.output.SetValue(msg)
        print(msg)


    def savel(self,event):
        text=wx.TextEntryDialog(self,'Give filename')
        if text.ShowModal()==wx.ID_CANCEL:
            wx.MessageBox('No Input Given')
            return
        file=text.GetValue()
        filepath=filename+'\\'+file
        msg=self.output.GetValue()
        if len(msg)==0:
            wx.MessageBox('No Output Text Given')
            return
        y=open(filepath,'w')
        y.write(msg)
        y.close()

class app(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show()
        return True

a=app()
a.MainLoop()
