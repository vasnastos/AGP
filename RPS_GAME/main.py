import game as gm
def main():
    print('Game starts')
    g=gm.game()
    g.round()
    print('Player:'+str(g.Player()))
    print('Computer:'+str(g.Computer()))

if __name__=='__main__':
    main()