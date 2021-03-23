from functools import reduce
list=[1,2,3,4,6,7,8]
print(list)
print(len(list))
print('Summary='+str(sum(list)))
print('Max='+str(max(list)))

def ascii_sum(x):
    sum=0
    for i in x:
       sum+=ord(i)
    return sum


list=['vasilis','maria','nikos','vaggelis']
print(list)
print(max(list,key=len))
print(reduce(lambda y,x:y+ascii_sum(x),list,0))