import logging as log
from pathlib import Path
import random as r
import threading as th
import os

global logger
global fh
global sh

logger=log.getLogger("App_tester")
logger.setLevel(log.DEBUG)
fh=log.FileHandler('app_in.log')
logger.addHandler(fh)
formater=log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formater)
sh=log.StreamHandler()
sh.setFormatter(formater)
logger.addHandler(sh)


def filelogger(filename):
    try:
        print(os.getcwd())
        with open(filename,'r') as f:
            data=f.readlines()
        logger.info(f'file:{filename} found\n   *Lines:{(len(data))}\n   *File Size:{Path(filename).stat().st_size}Kb')
        print('execute')
    except FileNotFoundError:
        logger.info('file:'+str(filename)+' not found')
    logger.debug(f'loggind level function with id:{r.randint(1000,900000)} exceeded succesfully\n\n')

def threadHandler(books):
    for k in books:
        filelogger(k)

def main():
    jobs=list([])
    threads=4
    bookshandler=[]
    for i in range(int(threads)):
        bookshandler.append(list([]))
    threadcounter=0
    for i in range(12):
        if int(threadcounter)==int(threads):
            threadcounter=0
        bookshandler[int(threadcounter)].append('sample'+str(int(i))+'.txt')
        threadcounter+=1
    for id in range(int(threads)):
       threadmaker=th.Thread(target=threadHandler(bookshandler[int(id)]),name='Thread_'+str(int(id)+1))
       jobs.append(threadmaker)
    for j in jobs:
        print('thread '+j.getName()+' start the processing')
        j.start()
    for j in jobs:
        j.join()

if __name__=='__main__':
    main()