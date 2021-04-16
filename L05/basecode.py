import os
import re
from time import time
import termcolor as tm

parentroot='REPOSITORIES/oop-master'

def file_parser():
    starttime=time()
    allfiles=[]
    try:
        for path,_,file in os.walk(top=parentroot,topdown=True):
            allfiles+=[path+'/'+l for l in file if l.endswith('.cpp') or l.endswith('.c') or l.endswith('.hpp') or l.endswith('.h')]
    except Exception:
        print('Can not open folder oop-master')
        return list([])
    tm.cprint('Elapsed Time for file opening:'+str(time()-starttime)+' s','red')
    return allfiles

files=file_parser()


def filesbycategory():
    counter={'cpp':0,'hpp':0,'h':0,'c':0}
    starttime=time()
    for x in files:
        if re.match('.+\.cpp$',x): 
            #if x.endswith('.cpp'):
            counter['cpp']+=1
        elif x.endswith('.hpp'):
            counter['hpp']+=1
        elif x.endswith('.h'):
            counter['h']+=1
        else:
            counter['c']+=1
    
    for key in counter:
        tm.cprint('\t'+str(key)+'-->'+str(counter[key]),'green')
    tm.cprint('=='*30,'white')
    endtime=time()
    tm.cprint('Lapsed Time:'+str(endtime-starttime)+' s','red')

def codelines():
    starttime=time()
    linecounter=0
    for i in files:
        with open(i,'r',encoding="utf-8",errors='ignore') as f:
            for j in f:
                if len(j.strip())!=0:
                    linecounter+=1
    tm.cprint('Lines of code:'+str(linecounter),'red')
    tm.cprint('Elapsed Time for finding all lines of code:'+str(time()-starttime)+'\'s','red')

  
#filesbycategory()
#print('=='*30)
codelines()
#print('=='*30)

