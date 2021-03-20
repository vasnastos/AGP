from time import time
import random as r
import logging as log

mvs={0:'R',1:'P',2:'S'}
r.seed(time()*1000)

def valid(playerinput):
    if str(playerinput)=='R' or str(playerinput)=='S' or str(playerinput)=='P':
        return True
    else:
        print('Not a valid move!!!')
        return False

#Construct Logger


class rps:
    def __init__(self):
        self.computerwins=0
        self.playerwins=0
        self.rounds=0
        self.playermove=''
        self.computermove=''
        self.roundcounter=0
        self.win=''
        self.logger=log.getLogger('RPS_LOGGER')
        self.logger.setLevel(log.DEBUG)
        sh=log.StreamHandler()
        fh=log.FileHandler('RPS.log')
        formatter=log.Formatter('%(asctime)s--%(levelname)s-%(message)s')
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def standard_moves(self,ply,cmp):
         self.playermove=ply
         self.computermove=cmp
         if str(ply)==str(cmp):
             return
         elif (str(ply)=='R' and str(cmp)=='S') or (str(ply)=='S' and str(cmp)=='P') or (str(ply)=='P' and str(cmp)=='R'):
             self.playerwins+=1
         else:
             self.computerwins+=1
    
    def set_Num_Of_Rounds(self,rnds):
       self.playerwins,self.computerwins,self.rounds,self.roundcounter=0,0,rnds,1

    def winner(self):
        if str(self.playermove)==str(self.computermove):
            self.win='t'
            self.logger.info("Winner:Tie\n---------------------------------------------------\n\n")
            return
        elif str(self.playermove)=='R' and str(self.computermove)=='S':
             self.win='p'
             self.playerwins+=1
        elif str(self.playermove)=='P' and str(self.computermove)=='R':
             self.playerwins+=1
             self.win='p'
        elif str(self.playermove)=='S' and str(self.computermove)=='P':
             self.playerwins+=1
             self.win='p'
        else:
            self.computerwins+=1
            self.win='c'
        self.logger.info('Winner:'+str(self.win)+'\nPlayer:'+str(self.playerwins)+'\tComputer:'+str(self.computerwins)+'\n--------------------------------------------------------------------\n\n')
            
    def round(self,move):
            if int(self.roundcounter)==int(self.rounds):
                self.logger.info('Game Ended')
                self.logger.info('Final Score\nPlayer:'+str(self.playerwins)+'\tComputer:'+str(self.computerwins))
                return
            x=r.randint(0,2)
            self.computermove=mvs[int(x)]
            print(self.computermove)
            self.playermove=move
            self.logger.info('Player Move:'+str(self.playermove))
            self.winner()
            self.roundcounter+=1
    
    def display(self):
        print('Player Wins:'+str(self.playerwins)+'\tComputerWins:'+str(self.computerwins))
    
    def __str__(self):
       return 'Player Wins:'+str(self.playerwins)+'\tComputerWins:'+str(self.computerwins)

def main():
    rpsobject=rps()
    rpsobject.rounds()
    print(rpsobject)
