class node:
    def __init__(self,a_data):
        self.data=a_data
        self.next=None
    def Data(self):
        return self.data

class List:
    def __init__(self):
        self.head=None
    def pushBack(self,dt):
        if self.head==None:
            self.head=node(dt)
            return
        i=self.head
        while i.next!=None:
            i=i.next
        n=node(dt)
        i.next=n

    def length(self):
        counter=0
        i=self.head
        while i!=None:
            counter+=1
            i=i.next
        return counter

    def Show(self):
        i=self.head
        while i!=None:
            print(str(i.Data()))
            i=i.next

def main():
    l=List()
    for j in range(1,10):
       l.pushBack(j)
    l.pushBack('Hello')
    l.pushBack('This')
    l.Show()
    print('List Length:'+str(l.length()))

if __name__=='__main__':
    main()