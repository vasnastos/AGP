import random 

# Λίστα με αριθμούς από το 1-1000
def create_random_numbers(number_of_samples:int,max_num:int):
    alist=[]
    #alist=list()
    for _ in range(number_of_samples):
        alist.append(random.randint(1,max_num))
    return alist


if __name__=='__main__':
    print(create_random_numbers(20,2000))
    print(create_random_numbers(30,3000))