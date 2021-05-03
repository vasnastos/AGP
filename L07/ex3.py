#pip install matplotlib,pip install numpy
import os
import random as r
import pandas as pd
import matplotlib.pyplot as plt
from time import time
import numpy as np
r.seed(time())


def File_Decode():
    files=dict({})
    path=os.path.join('','EX_3')
    for _,_,fls in os.walk(path,topdown=True):
        for k in fls:
            end=k.split('.')[len(k.split('.'))-1]
            if end in files:
                files[end]+=1
            else:
                files.update({end:1})
    return files

def make_colors(cnt):
    return [(r.randint(0,255)/255,r.randint(0,255)/255,r.randint(0,255)/255) for i in range(cnt)]

 
def main():
   allfiles=File_Decode()
   colors=make_colors(len(allfiles))
   keys=list(allfiles.keys())
   merged=[(keys[i],colors[i]) for i in range(len(colors))]
   df=pd.DataFrame(merged,columns=['File','Color'])
   print(df)
   plt.bar(list(allfiles.keys()),allfiles.values(),color=colors)
   plt.title('files EX_3 folder Decoder')
   plt.xlabel('File',fontsize=21)
   plt.ylabel('Counter',fontsize=21)
   plt.show()

main()  