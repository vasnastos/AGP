import random as r

value='DIT UOI ARTA INFORMATICS AND TELECOMMUNICATIONS'

lb=r.randint(0,len(value)-1)
rb=r.randint(0,len(value)-1)

if lb>rb:
    temp=lb
    lb=rb
    rb=temp

print(value[lb:rb])