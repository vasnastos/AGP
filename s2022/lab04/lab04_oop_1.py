import os
from prettytable import PrettyTable,ALL

class Car:
    def __init__(self,b,m,y):
        self.brand=b
        self.model=m
        self.year=y
    
    def __str__(self):
        return self.brand+"-"+self.model+"-"+str(self.year)

def show_cars(cars:list):
    table=PrettyTable(["MODEL","BRAND","YEAR"])
    table.hrules=ALL
    for c in cars:
        table.add_row([c.model,c.brand,c.year])
    print(table,'\n\n')


if __name__=='__main__':
    cars=[]
    with open(os.path.join('..','Source','cars.txt')) as RF:
        for line in RF:
            data=line.split(",")
            cars.append(Car(data[2].strip(),data[1],int(data[0])))
    
    sort_cars_by_year=sorted(cars,key=lambda c:c.year)
    sort_cars_by_brand=sorted(cars,key=lambda c:c.brand)
    
    print("SORT BY YEAR")
    show_cars(sort_cars_by_year)
    print("SORT BY BRAND")
    show_cars(sort_cars_by_brand)
