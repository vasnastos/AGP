import random as r

available=['R','P','S']

class game():
    def __init__(self):
        print('Object made:'+str(self))
        self.player=''
        self.computer=''
    def round(self,inp):
        self.player=inp
        pos=r.randint(0,2)
        self.computer=available[int(pos)]
    def winner(self,inp):
        if inp.upper() not in available:
            return 'Not a valid move'
        self.round(inp)
        if str(self.player)==str(self.computer):
            return 'Tie Game'
        elif str(self.player)=='R' and str(self.computer)=='S':
            return 'player wins'
        elif str(self.player)=='S' and str(self.computer)=='P':
            return 'player wins'
        elif str(self.player)=='P' and str(self.computer)=='R':
            return 'player wins'
        else:
            return 'computer wins'

