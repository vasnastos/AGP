mytuple=(1,2,3,4,5,6,7,9,10)
print('Len:'+str(len(mytuple)))
(first,*k,last)=mytuple
print(first)
print(k)
print(last)