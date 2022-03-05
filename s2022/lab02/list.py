from statistics import mean

def list_comprehension_sample():
    mylist=[56, 37, 771, 90, 16, 11]
    new_list_1=[len(str(x)) for x in mylist]
    new_list_2=[str(x)[::-1] for x in mylist]
    new_list_3=[x for x in mylist if x>mean(mylist)]
    new_list_4=[(x,True if x%2==0 else False) for x in mylist]
    return new_list_1, new_list_2, new_list_3,new_list_4

if __name__ == '__main__':
    n1,n2,n3,n4=list_comprehension_sample()
    print(n1)
    print(n2)
    print(n3)
    print(n4)