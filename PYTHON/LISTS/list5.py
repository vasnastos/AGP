import random as r
from time import time

r.seed(time()*1000)

size=r.randint(5,12)
mylist=[r.randint(2,200) for i in range(size)]
sortedrusult=sorted(mylist)

countloops=0
start=time()
while mylist!=sortedrusult:
    r.shuffle(mylist)
    countloops+=1

end=time()
print(f'Table Contains:{size} numbers')
print(mylist)
print(sortedrusult)
print('Total Loops:{}'.format(countloops))
print('Lapsed Time:{}\'s'.format(end-start))