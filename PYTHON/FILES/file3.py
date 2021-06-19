import os
import csv
from tabulate import tabulate

path=os.path.join('..','DATA','codes.csv')
with open(path,'r') as RF:
    reader=csv.reader(RF)
    data=list()
    start=True
    for row in reader:
        data.append(row)
print(tabulate(data,headers=['COUNTRY','CODE'],tablefmt='fancy_grid'))

y=open(path,'r')
print([x.strip() for x in y.readlines()],end='\n\n')
y.close()

y=open(path,'r')
k=y.readline()
while k!='':
    print(k.strip())
    k=y.readline()
y.close()