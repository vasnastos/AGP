filepath='file(csv)/students.csv'

def average(list):
    sum=0
    for x in list:
        k=x.replace(',','.')
        sum+=float(k)
    return float(sum)/len(list)

def main():
    students={}
    y=open(filepath,'r')
    counter=1
    for v in y:
        values=v.strip()
        data=[]
        for x in values.split(';'):
            data.append(x)
        students[counter]=data
        counter+=1
    y.close()
    for x in students:
      print('Student_'+str(x))
      print(students[x])
    filename=input('Give filename you want to save the average:')
    z=open('file(csv)/average.csv','w')
    z.write('Student;Average\n')
    counter=1
    for x in students:
        print('Student_'+str(counter)+'-'+str(average(students[x])))
        z.write(str(counter)+';'+str(average(students[x]))+'\n')
        counter+=1     

if __name__=='__main__':
    main()