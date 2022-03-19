import os

def show_students(students:list):
    for student in students:
        print(student)

def average_math(students:list):
    s=0
    for student in students:
        s+=int(student[5])
    return s/(len(students))

def average_reading(students:list):
    s=0
    for student in students:
        s+=int(student[6])
    return s/(len(students))

def average_writing(students:list):
    s=0
    for student in students:
        s+=int(student[7])
    return s/(len(students))

def sum_up_average_scores(students:list,math=False,reading=False,writing=False):
    av_index=5 if math else 6 if reading else 7 if writing else None
    if av_index==None: return -1
    return sum([int(student[av_index]) for student in students])/len(students)

def show_average_per_students(students:list):
    for index,student in enumerate(students):
        print(f"Student {index}-->Math:{student[5]},Reading:{student[6]},Writing:{student[7]},Average:{(int(student[5])+int(student[6])+int(student[7]))/3}")


if __name__ == "__main__":
    start=True
    students=list()
    with open(os.path.join('..','..','Datasets','StudentsPerformance.csv')) as RF:
        for line in RF:
            if start:
                start=False
                continue
            data=[d.replace("\"","").strip() for d in line.split(',')]
            students.append(tuple(data))
    
    #εμφάνιση φοιτητών
    print("Checkpoint 1")
    show_students(students)
    print('\n')

    print("Checkpoint 2")
    print(f"Average math score:{average_math(students)}")
    print(f"Average reading score:{average_reading(students)}")
    print(f"Average writing score:{average_writing(students)}",end='\n\n')


    print("Checkpoint 3")
    print(f"Average math score:{sum_up_average_scores(students,math=True)}")
    print(f"Average reading score:{sum_up_average_scores(students,reading=True)}")
    print(f"Average writing score:{sum_up_average_scores(students,writing=True)}",end='\n\n')

    print("checkpoint 4")
    show_average_per_students(students)


