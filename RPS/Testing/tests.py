import unittest as un

computer=0
player=1
tie=2

def rps(x,y):
    if str(x)==str(y):
        return tie
    elif str(x)=='Rock' and str(y)=='Scissors':
         return player
    elif str(x)=='Paper' and str(y)=='Rock':
        return player
    elif str(x)=='Scissors' and str(y)=='Paper':
        return player
    else:
        return computer

class testing(un.TestCase):
    def Play(self):
        self.assertEqual(rps('Rock','Scissors'),player)
        self.assertEqual(rps('Scissors','Scissors'),tie)
        self.assertTrue(rps('Paper','Scissors')==computer)
        self.assertEqual(rps('Paper','Rock'),player)
        self.assertEqual(rps('Scissors','Rock'),computer)


un.main()
    
#Debug
#info
#Warning
#Error
#Critical