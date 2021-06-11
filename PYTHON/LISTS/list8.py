import collections
mylist=[10,10,10,10,20,20,20,20,40,40,50,50,30,20,40,10,15,15,90,50,90,15]
counter=dict()
for x in mylist:
    if x in counter:
        counter[x]+=1
    else:
        counter[x]=1
for key in counter:
    print(f'{key}-->{counter[key]}')
# Because Its Python Time
# counter=collections.Counter(mylist)
# print(counter)