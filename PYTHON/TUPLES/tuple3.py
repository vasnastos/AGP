atuple=('VASILIS','NASTOS','ARTA','6912345678')
stuple=atuple
"""
stuple[2]='IGOUMENITSA'
Traceback (most recent call last):
  File "s:\AGP\PYTHON\TUPLES\tuple3.py", line 3, in <module>
    stuple[2]='IGOUMENITSA'
TypeError: 'tuple' object does not support item assignment
"""

"""
print(atuple[5])
Traceback (most recent call last):
  File "s:\AGP\PYTHON\TUPLES\tuple3.py", line 10, in <module>
    print(atuple[5])
IndexError: tuple index out of range
"""
print(stuple)

print('\n\nAlternative')
for i in atuple:
    print(i)

#LIST WITH TUPLES
print('\n\nAlternative')
mylist=[('NIKOS','PAPPAS','1'),('AGGELOS','DIMITSAS','2'),('VASILEIOS','NASTOS','3'),('DIMITRIS','EYAGGELOY','4')]
for name,surname,code in mylist:
    print(name,surname,code)

#SORT A LIST WITH TUPLES BY CODE
def Sort(alist):
    import random
    random.shuffle(alist)
    print(alist)
    alist=sorted(alist,key=lambda key:key[2])
    print(alist)

Sort(mylist)
