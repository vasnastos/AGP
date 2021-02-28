import random as r
x="Τμήμα πληροφορικής και τηλεπικοινωνιών"
x.encode('utf-8')
print('1.By letter output')
for k in x:
    print('letter:'+k)
#SLICING
length=len(x)
lb=r.randint(0,int(length)-1)
up=r.randint(0,int(length)-1)
if up>lb:
    temp=lb
    lb=up
    up=lb
#2
print('2.Sliced String')
print(x[lb:up])
#3.in
print('3.'+'τμημα' in x)
#not in
#4.:n slicing
print('4.'+x[:5])#Τμήμα
#5.:n: slicing
print('5.'+x[10:])#οφορικής και τηλεπικοινωνιών
#6.Negative Slicing
print('6.'+x[-5:-1])#ωνιώ

#UpperCase String
print(x.upper())

k="Hello World from Python"
#7.Striping
print('7.'+k.strip())
#8.String Replacement
print(x.replace('o','n'))

#9.Split a string
v="one,two,three,four,five"
splitdata=v.split(',')#List
print('9.String Split')
for x in splitdata:
    print(x)

#10.String adding
x="hello"
y=','
z="world"
print('10.'+x+y+z)
#11.String and multiplication
print('11.'+3*x)

#12.String format
dollar=5
type='euros'
myorder="The order i made costs my {} {}"
print('12.'+myorder.format(dollar,type))


"""
String methods available at:https://www.w3schools.com/python/python_strings_methods.asp
"""

#13.Starts and ends with
x="this is a prefix text"
print('13.')
print('Starts with t:'+str(x.startswith('t')))
print('ends with ing:'+str(x.endswith('ing')))