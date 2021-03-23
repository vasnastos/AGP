import random as r

x='Τμήμα πληροφορικής και τηλεπικοινωνιών(Dit Uoi)'

print(x.upper())
print(x.endswith(')'))
print(x.isalpha())

print(x.replace(' ','_'))

print(x.find('Dit'))

print('Random sub string')
k=r.randint(0,len(x)-1)
y=r.randint(0,len(x)-1)
if int(y)<int(k):
   t=k
   k=y
   y=t
print(x[int(k):int(y)])
print(x[-5:-1])
print(x.split(' '))

x='Hello'
y=' World'
print(x+y)