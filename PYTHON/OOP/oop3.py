from random import randint
import datetime
from tabulate import tabulate

moves=['R','P','S']

class RPS:
    def __init__(self):
        self.pw=0
        self.cw=0
        self.game=list()
    
    def Round(self):
        print('TimeStamp',datetime.datetime.now().strftime('%Y/%m/%d--%H:%M:%S'))
        player=input('Give your Move(R|P|S):')
        player=player.upper()
        while player not in moves:
            player=input('Invallid Move\nGive your Move(R|P|S):')
        print('\n\n')
        computer=moves[randint(0,2)]
        outcome=''
        if player==computer:
            print('Tie Round')
            outcome='TG'

        elif (player=='R' and computer=='S') or (player=='S' and computer=='P') or (player=='P' and computer=='R'):
            print('Player Wins')
            outcome='PW'
            self.pw+=1
        else:
            outcome='CW'
            print('Computer wins')
            self.cw+=1
        self.game.append([player,computer,outcome])
        print(tabulate(self.game,headers=['PLAYER','COMPUTER',''],tablefmt='fancy_grid'),end='\n\n')
    

    def Rounds(self,size):
        for _ in range(size):
            self.Round()
        self.game.append([self.pw,self.cw,'TOTAL'])
        print(tabulate(self.game,headers=['PLAYER','COMPUTER',''],tablefmt='fancy_grid'))


if __name__=='__main__':
    G=RPS()
    s=int(input('Give number of rounds:'))
    print('\n\n')
    G.Rounds(s)