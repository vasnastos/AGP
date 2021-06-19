from tabulate import tabulate

class shape:
    def __init__(self,name,r):
        self.name=name
        self.radius=r
    
    def __str__(self):
        return f'{self.name},{self.radius}'
    
    
class Sphere(shape):
    def __init__(self,n,r):
        super().__init__(n,r)
    
    def Volume(self):
        return (4/3)*3.14*(self.radius**3)
    
    def Area(self):
        return 4*3.14*(self.radius**2)
    
    def __lt__(self,bo):
        return self.Area()<bo.Area()

    def __TOLIST__(self):
        return [self.name,self.radius,self.Volume(),self.Area()]

class circle(shape):
    def __init__(self,n,r):
        super().__init__('circle',r)

    def Volume(self):
        return 3.14*(self.radius**2)

    def Area(self):
        return 3.14*(self.radius**2)
    
    def __lt__(self,bo):
        return self.Area()<bo.Area()

    def __TOLIST__(self):
        return [self.name,self.radius,self.Volume(),self.Area()]

import random
from time import time
random.seed(time()*1000)

shp=['circle','sphere']

def Print_List(shapes):
    data=[c.__TOLIST__() for c in shapes]
    print(tabulate(data,headers=['SHAPE','RADIUS','VOLUME','AREA'],tablefmt='fancy_grid'),end='\n\n')

if __name__=='__main__':
    shapes=list()
    for _ in range(20):
        choice=random.randint(1,2)
        if choice==1:
            shapes.append(circle(shp[choice-1],random.randint(2,30)))
        else:
            shapes.append(Sphere(shp[choice-1],random.randint(2,30)))
    Print_List(shapes)
    print('Sorted Tables')
    print('**'*30)
    shapes=sorted(reversed(shapes))
    Print_List(shapes)

