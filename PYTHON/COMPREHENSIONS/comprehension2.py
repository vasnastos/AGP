# Εκτύπωση λίστας με άρτιους αριθμούς

mylist=[x for x in range(1,21)]
print([x for x in mylist if x%2==0])


#1.Ποιο θα είναι το αποτέλεσμα?
mylist=['DIT','DEPARTMENT','L','M','UOI','TELECOMMUNICATIONS']
result=[x for x in mylist if len(x)>3]
print('1.',result)
#-->

#2.Ποιο θα είναι το αποτέλεσμα?
mylist=['IOANNINA','ARTA','IGOYMENITSA','PREVEZA']
result=[x for x in mylist if x.startswith('I')]
print('2.',result)
#-->

#3.Ποιο το αποτέλεσμα?
