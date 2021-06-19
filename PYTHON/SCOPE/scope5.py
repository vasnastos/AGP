def Summary(alist):
  import random as r
  newlist=alist.copy()#shallow copy
  for i in range(len(newlist)):
      newlist[i]=r.randint(0,1000)
  print(newlist)
  return sum(newlist)

mylist=[1,2,3,4,56,6,7,8,9,12,1,34,6,7,8]
print(Summary(mylist))
print(mylist)