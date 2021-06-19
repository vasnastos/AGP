def Summary(alist):
    import random as r
    for i in range(len(alist)):
      alist[i]=r.randint(0,1000)
    return sum(alist)

mylist=[1,2,3,4,56,6,7,8,9,12,1,34,6,7,8]
print(Summary(mylist))
print(mylist)