#security code check
import re
#dictionary
power={0:'code does not support preconditions',1:'weak',2:'medium',3:'strong',4:'powerful'}

x=input('Give a code:')
y=x.lower()
uppers=False
counter=0
msg='Password Control\n'
msg+='------------------------\n'
for k in x:
    if k.isupper():
       uppers=True
       break

if uppers:
    msg+='Contains at least one uppercase Character:yes\n'
    counter+=1
else:
    msg+='Contains at least one uppercase Character:no\n'

if re.match('.*[0-9][0-9]*.*',x):
    msg+='Contains at least one digit:yes\n'
    counter+=1
else:
    msg+='Contains at least one digit:no\n'

found=True
if re.match('[A-Za-z0-9][A-Za-z0-9]*',x):
    found=False
print(found)
if found:
    msg+='Contains at least a special character:yes\n'
    counter+=1
else:
    msg+='Contains at least a special character:no\n'

if len(x)>8:
    msg+='Password Length over 8 Characters:yes\n'
    counter+=1
else:
    msg+='Password Length over 8 Characters:no\n'

print('Preconditions')
print(msg)
print('==================================')
print('\t\tPassword Power:'+str(power[int(counter)]))