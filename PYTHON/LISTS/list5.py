import random as r
from time import time

r.seed(time()*1000)

size=r.randint(5,12)
mylist=[r.randint(2,200) for i in range(size)]
sortedresult=sorted(mylist)

countloops=0
start=time()
while mylist!=sortedresult:
    r.shuffle(mylist)
    countloops+=1

end=time()
print(f'Table Contains:{size} numbers')
print('Table Contains:'+str(size)+' numbers')
print('Table Contains:',size,' number')
print('Table Contains %i numbers' %(size))
print(mylist)
print(sortedresult)
print('Total Loops:{}'.format(countloops))
print('Lapsed Time:{}\'s'.format(end-start))