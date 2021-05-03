from functools import reduce
import random

def MapReducer(map):
    #find summary of map vals
    summary=reduce(lambda y,elem:y+elem[1],map.items(),0)
    print(f'summary of map values:{summary}')

def MapSorter(map):
    newmap=dict(sorted(map.items(),key=lambda elem:elem[1]))
    print('Sorted Map')
    print(newmap)

def FilteredMap(map):
    newmap=dict(filter(lambda elem:elem[1]>5,map.items()))
    print('Filtered Map')
    print(newmap)


if __name__=='__main__':
    amap=dict({})
    for i in range(65,91):
        amap.update({chr(i):i})
    print(amap)
    MapReducer(amap)
    MapSorter(amap)
    FilteredMap(amap)
    aset=set({})
    for i in range(1,10):
        aset.add(i)
        aset.add(i)
    
    summary=reduce(lambda y,x:y+x,aset,0)
    print('set SUmmary:'+str(summary))