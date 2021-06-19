def ChangeList(alist):
    alist.clear()
    alist.append(1)
    alist.append(2)
    alist.append(3)


mylist=[1,2,3,4,5,6,7,8,9,10]
ChangeList(mylist)
print(mylist)

mylist2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
ChangeList(mylist.copy())
print(mylist)

mylist3=mylist
mylist3[0]=101
print(mylist,mylist,mylist==mylist3)
