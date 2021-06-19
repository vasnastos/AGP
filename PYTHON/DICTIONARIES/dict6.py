"""
employees = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
Εύρεση μέσου μισθού υπαλλήλων
"""
employees = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

s=0
for employee in employees:
    s+=employees[employee]['salary']
print('Avarage Salary:{}'.format(s/len(employees)))

print('Avarage Salary:{}'.format(sum([employee['salary'] for employee in employees.values()])/len(employees)))


