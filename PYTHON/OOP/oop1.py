class Person:
    objectcounter=0
    def __init__(self,n='',a=''):
        self.name=n
        self.age=a
        Person.objectcounter+=1
    
    def __str__(self):
        return f'{self.name}:{self.age}'

if __name__=='__main__':
    P1=Person()
    P2=Person('vasilis')
    P3=Person('vasilis',22)
    print(str(P1))
    print(str(P2))
    print(str(P3))
    print(f'Objects Created:{Person.objectcounter}')