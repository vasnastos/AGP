import logging as log
import random as r

#create a logger
global logger
global fh
global sh
logger=log.getLogger('RPS_Logger')
logger.setLevel(log.DEBUG)
fh=log.FileHandler('rps.log')
sh=log.StreamHandler()
formater=log.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')
fh.setFormatter(formater)
sh.setFormatter(formater)
logger.addHandler(fh)
logger.addHandler(sh)

#global variables
roundcount=1
playerwins,computerwins=0,0

#random seed
r.seed()

def rps(player,computer):
    global roundcount
    global playerwins,computerwins
    result=' *Round '+str(roundcount)+' exceeded\tResult:'
    if str(player)==str(computer):
        logger.info(result+'tie\n')
    elif (str(player)=='R' and str(computer)=='S') or (str(player)=='S' and str(computer)=='P') or (str(player)=='P' and str(computer)=='R'):
        logger.info(result+'Player Wins\n')
        playerwins+=1
    else:
        logger.info(result+'Computer Wins\n')
        computerwins+=1
    game='Round_'+str(roundcount)+' score table\n'
    game+='**************************************\n'
    game+='\t\tPlayer\tComputer\n'
    game+='\t\t   '+str(playerwins)+'   \t'+str(computerwins)+'\n---------------------------------------------'
    logger.info(game)
    logger.debug('Process pseudo reduce:'+str(r.randint(1000,999999))+' pid\n\n')
    roundcount+=1

def winner():
    outcome='After '+str(roundcount)+' the outcome is:'
    if int(playerwins)>int(computerwins):
        outcome+='Player Wins\n'
    elif int(playerwins)<int(computerwins):
        outcome+='Computer Wins\n'
    else:
        outcome+='Tie Game\n'
    logger.info(outcome)

Rps=['R','P','S']

def PlayerMove():
    print('Moves:')
    counter=1
    for x in Rps:
        print(str(counter)+'.'+str(x))
        counter+=1
    print('--------------------------')
    x=input('Select your move:')
    print('\n')
    if int(x)<=0 or int(x)>len(Rps):
        return PlayerMove()
    else:
        return Rps[int(x)-1]

def ComputerMove():
    return Rps[r.randint(0,2)]

def totalRounds():
    rnds=input('Give number of rounds(random-->for random rounds(limit:7   bound:30))')
    totalrounds=0
    if str(rnds)=='random':
        totalrounds=r.randint(7,30)
    else:
        totalrounds=int(rnds)
    return totalrounds

def Game():
    total=totalRounds()
    for i in range(total):
        rps(PlayerMove(),ComputerMove())
    winner()

if __name__=='__main__':
    Game()


        
   