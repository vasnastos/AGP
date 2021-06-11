import statistics
mylist=list()

def isPrime(value):
    counter=2
    for i in range(2,value-1):
        if value%i==0:
            counter+=1
    return counter==2

for i in range(1,20):
    mylist.append(i)

print(f'Median Value:{statistics.median(mylist)}')

primelist=[x for x in mylist if isPrime(x)]
print(primelist,end='\n\n')

mylist=list(set(mylist).difference(set(primelist)))
print(mylist)