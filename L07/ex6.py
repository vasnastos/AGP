#File Opening
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

source=os.path.join('','Datasets','source.csv')

def openFunc():
     y=open(source,'r')
     k=y.readline()
     elems=[]
     data=[]
     while k!='':
         data.append(k)
         k=y.readline()
     y.close()
     cols=[x.strip() for x in data[0].split(',')]
     data.remove(data[0])
     for m in data:
         c=m.split(',')
         elems.append((c[0],c[1],c[2],c[3].strip()))
     daf=pd.DataFrame(elems,columns=cols)
     print(daf)

def csvReader():
    data=None
    headers=[]
    contains=[]
    with open(source,'r') as R:
        data=csv.reader(R,delimiter=',')
        found=0
        for x in data:
            if found==0:
                headers=list(x)
                found=1
                continue
            contains.append(tuple(x))
    Ages=[]
    for _,_,age,_ in contains:
         if age not in Ages:
             Ages.append(age)
    counter=1
    for age in Ages:
        print(f'{counter}.{age}')
        counter+=1
    k=input('Select a plotting age:')
    selectedage=Ages[int(k)-1]
    vals={}
    for _,group,age,val in contains:
        if age==selectedage:
            vals.update({group:float(val)})
    plt.bar(vals.keys(),vals.values())
    plt.title(f'People at Age:{selectedage} Bar')
    plt.xlabel('Group')
    plt.ylabel('Value')
    plt.show()


def main():
    openFunc()
    csvReader()


main()

"""
  Other types:
  -->https://www.geeksforgeeks.org/reading-excel-file-using-python/
  -->https://blog.finxter.com/how-to-open-a-pdf-file-in-python/
  -->https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
  -->https://geekflare.com/python-yaml-intro/
"""