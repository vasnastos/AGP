import random 
from tabulate import tabulate
class TESTC:
   def __init__(self,i,p=0):
       self.id=i
       self.point=p if p!=0 else random.randint(1,10000)
    
   def __hash__(self):
       return int(self.id)
    
   def __lt__(self,p):
       return self.point<p.point
   
   def __reduce__(self,p):
       return TESTC(self.id,self.point+p.point)
   
   def __add__(self,p):
       return TESTC(self.id,self.point+p.point)

   def __eq__(self, o):
       return self.id==o.id
    
   def __ToTAB__(self):
       return [self.id,self.point]

   def __str__(self):
       return f'Id:{self.id}\t Score:{self.point}'

def Print_List(pls):
    data=[p.__ToTAB__() for p in pls]
    print(tabulate(data,headers=['ID','POINTS'],tablefmt='fancy_grid',showindex='always'),end='\n\n')

if __name__=='__main__':
    players=[TESTC(str(random.randint(10000,200000))) for _ in range(20)]
    Print_List(players)
    splayers=sorted(players)
    #splayers=sorted(players,key=lambda k:k.point)
    Print_List(splayers)
    c=players[9]+TESTC('')
    print('Adding:::')
    print(str(c),end='\n\n')
    aset={c for c in players}
    print('\n'.join([str(c) for c in aset]))
    from functools import reduce
    print('Summary:',reduce(lambda y,el:y+el.point,players,0))
    

