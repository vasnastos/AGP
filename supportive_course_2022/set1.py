from random_numbers import create_random_numbers

if __name__ == '__main__':
    alist=create_random_numbers(max_num=10,number_of_samples=1000)
    aset=set()
    for num in alist:
        aset.add(num)
    print(f'{len(aset)=}',end='\n\n')
    print(aset)
    # OR
    print(set(alist))