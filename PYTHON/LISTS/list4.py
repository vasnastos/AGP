from functools import reduce
mylist=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Purple','Orange','DarkBlue','DarkRed']
copy=mylist.copy()
print(mylist)
print(copy)
sortedcopy=sorted(copy,key=lambda elem:reduce(lambda y,ch:y+ord(ch),elem,0))
lastcopy=list(filter(lambda elem:reduce(lambda y,ch:y+ord(ch),elem,0)>300,sortedcopy))
print(sortedcopy)
print(lastcopy)