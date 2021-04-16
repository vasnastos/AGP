import os
import termcolor as tm

pathfiles=[]
filecounter={'cpp':0,'hpp':0,'c':0,'h':0,'other':0}
hr=tm.colored('==='*20,'red')

def print_Dirs(masterpath):
    global pathfiles
    files=os.listdir(masterpath)
    for x in files:
      if os.path.isdir(masterpath+'/'+x):
        print_Dirs(masterpath+'/'+x)
      else:
          pathfiles.append(masterpath+'//'+x)

def show_files():
      for x in pathfiles:
         print(tm.colored(x,'red'))
      print(hr)

def Format_Parser():
    for x in pathfiles:
          if x.endswith('.cpp'):
                filecounter['cpp']+=1
          elif x.endswith('.hpp'):
                filecounter['hpp']+=1
          elif x.endswith('.h'):
                filecounter['h']+=1
          elif x.endswith('.c'):
                filecounter['c']+=1
          else:
                filecounter['other']+=1
    for x in filecounter:
          print(tm.colored(str(x)+' files-->','blue'),end='')
          print(tm.colored(str(filecounter[x]),'green'))
        

