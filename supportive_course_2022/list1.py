import random 

# Λίστα με αριθμούς από το 1-1000
def create_random_numbers(number_of_samples=-1,max_num=100):
    alist=[]
    #alist=list()
    if number_of_samples:
        listlen=random.randint(10,20)
    else:
        listlen=number_of_samples
    for _ in range(listlen):
        alist.append(random.randint(1,max_num))
    return alist

if __name__=='__main__':
    list1=create_random_numbers()
    list2=create_random_numbers(max_num=2000)

    #list len
    print("Checkpoint 1")
    print(f"{len(list1)=}")
    print(f"{len(list2)=}")
    print("\n\n")

    # merge two list
    print("Checkpoint 2")
    list3=list1.copy()
    list3.extend(list2)
    print(list3)
    print("\n\n")


    #sort lists
    print("Checkpoint 3")
    list1.sort()
    list2.sort()
    print(list1)
    print(list2)
    print("\n\n")
    # print(sorted(list1))
    # print(sorted(list2))

    #reverse list
    print("Checkpoint 4")
    list1.reverse()
    list2.reverse()
    print(list1)
    print(list2)
    print("\n\n")
    # print(reversed(list1))
    # print(reversed(list2))

    print("Checkpoint 5")
    list3=list1+list2
    print(list3)









