import logging as log
import random as r
import termcolor as tm

Rps=['R','P','S']
moves={}
roundcount=0
playerwins,computerwins=0,0


def rps(player,computer):
    global roundcount
    global playerwins,computerwins
    result=' *Round '+str(roundcount)+' exceeded\tResult:'
    playercolor,computercolor='',''
    if str(player)==str(computer):
        log.info(result+'tie\n')
        playercolor,computercolor='blue','blue'
    elif (str(player)=='R' and str(computer)=='S') or (str(player)=='S' and str(computer)=='P') or (str(player)=='P' and str(computer)=='R'):
        log.info(result+'Player Wins\n')
        playerwins+=1
        playercolor,computercolor='green','red'
    else:
        log.info(result+'Computer Wins\n')
        computerwins+=1
        playercolor,computercolor='red','green'
    game='Round_'+str(roundcount)+' score table\n'
    game+='**************************************\n'
    game+='\t\tPlayer\tComputer\n'
    game+='\t\t   '+str(playerwins)+'   \t'+str(computerwins)+'\n---------------------------------------------'
    log.info(game)
    log.debug('Process pseudo reduce:'+str(r.randint(1000,999999))+' pid\n\n')
    moves.update({roundcount:[tm.colored(player,playercolor),tm.colored(computer,computercolor)]})
    roundcount+=1

def scoretable():
    table='Scoretable logging'
    table+='\n\t\tPlayer\tComputer\n'
    tab="\t"
    table+='------------------------------------------\n'
    for x in moves:
        table+=str(tab)+'Round_'+str(int(x)+1)+'  '+str(moves[x][0])+' \t  '+str(moves[x][1])+'\n'
    log.info(table)

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

def winner():
    outcome='After '+str(roundcount)+' the outcome is:'
    if int(playerwins)>int(computerwins):
        outcome+='Player Wins\n'
    elif int(playerwins)<int(computerwins):
        outcome+='Computer Wins\n'
    else:
        outcome+='Tie Game\n'
    log.info(outcome)
    scoretable()

def ComputerMove():
    return Rps[r.randint(0,2)]

def Game():
    total=7
    for i in range(total):
        rps(PlayerMove(),ComputerMove())
    winner()

def Main():
    log.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=log.DEBUG)
    #write to file
    #log.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=log.DEBUG,filename='rock_paper_scissors.log',filemode='w')
    Game()


Main()