#------------------------------------------------------------------------------------#
# List is a collection which is ordered and changeable. Allows duplicate members.    #
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. #
# Set is a collection which is unordered and unindexed. No duplicate members.        #
# Dictionary is a collection which is ordered* and changeable. No duplicate members. #
#------------------------------------------------------------------------------------#

mytuple=('A',1,234,True,'DIT UOI')
print('LEN:{}'.format(len(mytuple)))
print(type(mytuple))
print('234-->{}'.format(mytuple.index(234)))

#Upacking-->Extract values in variable
(a,b,c,d,e)=mytuple
print(a,b,c,d,e)

# Αλλαγή του True σε False
mytuple=list(mytuple)
mytuple[3]=False
mytuple=tuple(mytuple)
print(mytuple)

#Προσθήκη της Λέξης University στο tuple
mytuple=list(mytuple)
mytuple.append('University')
mytuple=tuple(mytuple)
print(mytuple)