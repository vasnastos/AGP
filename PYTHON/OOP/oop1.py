class Person:
    objectcounter=0
    def __init__(self,n='',a=''):
        self.name=n
        self.age=a
        Person.objectcounter+=1
    
    def __str__(self):
        return f'Το όνομα μου είναι {self.name}:και είμαι {self.age} ετών'

if __name__=='__main__':
    P1=Person()
    P2=Person('vasilis')
    P3=Person('vasilis',22)
    print(P1.name,P1.age)
    print(P3)
    print(P2)
    print(P3)
    print(f'Objects Created:{Person.objectcounter}')