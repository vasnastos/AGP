import zipfile as zip
import os
import pip._vendor.requests
import urllib.request as url
import threading as th
from time import sleep
import progressbar as pbr
#pip install progressBar

pbar=None

def progressBar(block_num,block_size,total_size):
     global pbar
     if pbar is None:
          pbar=pbr.ProgressBar(maxval=total_size)
          pbar.start()
     downloaded=block_num*block_size
     if downloaded<total_size:
         pbar.update(downloaded)
     else:
         pbar.finish()
         pbar=None

source='https://github.com/vasnastos/Assignment_AGP/archive/refs/heads/master.zip'
retrivedpath=os.path.join('','Master')
if not os.path.exists(retrivedpath):
    os.mkdir(retrivedpath)
zipfile=os.path.join(retrivedpath,'master.zip')
ret=url.urlretrieve(source,zipfile,progressBar)


with zip.ZipFile(zipfile,'r') as Z:
    Z.extractall(retrivedpath)
print('folder created at '+str(retrivedpath))
removepath=os.path.join(retrivedpath,'master.zip')
os.remove(removepath)

print('Start Decoding........')

for x in os.walk(retrivedpath):
    for y in x[2]:
        print(y)
