#Dictionary Summary

mydict={'a':10,'b':20,'c':30,'d':40,'e':50}
print(mydict.get('f','f does not exists'),end='\n\n')

#Pop Item
print(mydict)
mydict.popitem()
print('Dictionary After Pop Out an Item')
print(mydict,end='\n\n')

#Update Dict
print(mydict)
mydict.update({'e':50})
mydict.update({'f':60})
print(mydict,end='\n\n')

#Iteratable Dict
print(mydict.items(),end='\n\n')

#Pop Specific Dictionary Record using its key
a='a'
print(mydict)
mydict.pop(a)
print(mydict,end='\n\n')

#If Key does not Exist i get an key error
#mydict.pop('j')
#----------
#mydict.pop('j')
#KeyError: 'j'

#In order to find maximun pair by value
print(max(mydict.items(),key=lambda elem:elem[1]))