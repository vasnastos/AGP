import math as m
def average(numbrs):
    sum=0
    for x in numbrs:
        sum+=x
    return float(sum)/len(numbers)

def Cv(numbers):
   avg=average(numbers)
   cv=0
   for x in numbers:
       cv+=m.pow(float(x)-float(avg),2)
   cv/=len(numbers)-1
   cv=m.sqrt(cv)/float(avg)
   return cv

numbers=[78.6,45.7,12.3,4.78,13.67,89.4,9.1,2.3,56.7]
print('\t\tList')
print(numbers)
print('Average:'+str(average(numbers)))
print('Coeffiecient of Variation:'+str(Cv(numbers)))
