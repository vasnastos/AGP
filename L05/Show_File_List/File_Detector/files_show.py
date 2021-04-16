import termcolor as tm
import os
import re as r

masterpath='oop-master'

def print_file(file,masterpath):
    print(tm.colored(file,'blue'),end='')
    print(tm.colored('('+masterpath+')','red'))

def print_Dirs(files,masterpath):
    for x in files:
      if os.path.isdir(masterpath+'/'+x):
        print_Dirs(os.listdir(masterpath+'/'+x),masterpath+'/'+x)
      else:
          print_file(x,masterpath)

def file_List():
    files=os.listdir(masterpath)
    print_Dirs(files,masterpath)

def main():
    print(tm.colored("Start file Parsing",'green'))
    print(tm.colored("Folder Checked:"+str(masterpath),'green'))
    print(tm.colored('='*15,'red'))
    file_List()


           