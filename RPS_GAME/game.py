#game class
import random as r

available=['R','P','S']

class game:
    def __init__(self):
        print('Constructor called:'+str(self))
        self.player=''
        self.computer=''
    def round(self):
        x=input('Select R(Rock)/P(Paper)/S(Scissors):')
        while x.upper() not in available:
            x = input('Select R(Rock)/P(Paper)/S(Scissors):')
        position=r.randint(0,2)
        self.player=x.upper()
        self.computer=available[int(position)]
        if str(self.player)==str(self.computer):
            print('Tie Game')
        elif str(self.player)=='R' and str(self.computer)=='S':
            print('Player wins')
        elif str(self.player)=='S' and str(self.computer)=='P':
            print('player wins')
        elif str(self.player)=='P' and str(self.computer)=='R':
            print('player wins')
        else:
            print('computer wins')
    def Player(self):
        return self.player
    def Computer(self):
        return self.computer