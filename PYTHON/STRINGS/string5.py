string="Department of informatics and telecommunications"
print(string.split())
secondstring=string.replace(' ','_')
print(secondstring.split('_'))
third="""
 Hello 
 world 
 from 
 algolab
"""
print(third.split('\n'))
print(secondstring[-13:-1])
print(third)

import random 
print(f'Three random numbers:{random.randint(1,200)}\t{random.randint(1,200)}\t{random.randint(1,200)}'.format())
print('Binary represantation of 24 is {0:b}'.format(24))

x='DIT_UOI'
print("".join(reversed(x)),x[::-1])