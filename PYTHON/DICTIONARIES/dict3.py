import requests as r

employees=dict()
alldata=r.get('https://raw.githubusercontent.com/vasnastos/AGP/master/PYTHON/DATA/employees.csv').text.split('\n')
for employee in alldata:
    if len(employee.strip())==0: continue
    emp,sal=employee.split(',')
    employees[emp]=float(sal)

#Average Salary
#-----------------------------------------------------------------------#
#avgsalary=sum(employees)/len(employees)                                #
#print('Average Salary:{}'.format(avgsalary))                           #
# Traceback (most recent call last):                                    #
#  File "s:\AGP\PYTHON\DICTIONARIES\dict3.py", line 11, in <module>     #
#    avgsalary=sum(employees)/len(employees)                            #
# TypeError: unsupported operand type(s) for +: 'int' and 'str'         #
#-----------------------------------------------------------------------#

from functools import reduce
average=reduce(lambda y,elem:y+elem[1],employees.items(),0)/len(employees)
print('Average Salary:{}'.format(average))

##Employees over Average Salary
counter=0
for employee in employees:
    if employees[employee]>average:
        counter+=1

print(f'{counter} employees have salary over {average}-->[Average]')