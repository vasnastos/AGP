# ΔΗΜΙΟΥΡΓΙΑ ΑΝΤΙΓΡΑΦΟΥ ΜΙΑΣ ΛΙΣΤΑΣ

mylist=[1,2,3,4,56,7,8,9,13]
blist=[x for x in mylist if x%2==0]
print(blist)
#-->4,56,8,2

# Α τρόπος
copy=mylist.copy()
print('Copy 1',copy,end='\n\n')

#B Τρόπος Comprehension
print([x for x in mylist])

#C Τρόπος
alist=list()
for x in mylist:
    alist.append(x)
print(alist)

#String to List
g='Human'
print([x for x in g])