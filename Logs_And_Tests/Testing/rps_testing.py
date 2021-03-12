import unittest

def game(player,computer):
    if str(player)==str(computer):
        return 0
    elif (str(player)=='R' and str(computer)=='S') or (str(player)=='S' and str(computer)=='P') and (str(str(player)=='P' and str(computer)=='R')):
        return 1
    else:
        return 2

def winner(inputs):
    player=0
    computer=0
    for x in inputs:
       played=game(inputs[x][0],inputs[x][1])
       if int(played)==1:
         player+=1
       elif int(played)==2:
         computer+=1
    if int(player)>int(computer):
        return 'player'
    elif int(player)<int(computer):
        return 'computer'
    else:
        return 'tie'

def Valid(container):
    return 'R' in container and 'S' in container and 'P' in container and len(container)==3

class Test(unittest.TestCase):
    def test_game1(self):
        self.assertEqual(int(game('R','S')),1,'Player Wins')
        self.assertEqual(int(game('S','R')),2,'Computer Wins')
        self.assertTrue(int(game('P','S'))==2,'Computer Wins')
        self.assertTrue(int(game('R','R'))==0,'Tie Game')

    def test_game2(self):
        self.assertGreater(game('R','S'),game('S','S'),'Result 1:Player Wins\t Result 2:Computer Wins')
        self.assertEqual(int(game('R','S')),1,'Player Wins')

    def test_game3(self):
        inps={1:['R','S'],2:['S','P'],3:['P','P'],4:['R','P']}
        self.assertEqual(str(winner(inps)),'player',msg='After '+str(len(inps))+' rounds player wins')

    def test_game4(self):
        self.assertTrue(Valid(['R','P','S']),str(len(['R','P','S']))+'Valid Moves')



if __name__=='__main__':
    unittest.main()