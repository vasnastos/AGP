if __name__=='__main__':
    aset=set()
    for i in [1,2,3,4,4,5,1,1,7,2,1,6,6,6,9,9,10,11,12,12,11,12,8,8,8,8]:
        aset.add(i)
    #aset={x for x in [1,2,3,4,4,5,1,1,7,2,1,6,6,6,9,9,10,11,12,12,11,12,8,8,8,8]}
    #aset=set([1,2,3,4,4,5,1,1,7,2,1,6,6,6,9,9,10,11,12,12,11,12,8,8,8,8])
    print(f'{len(aset)=}')
    for i in aset:
        print("==>",i)
    print(f"{sum(aset)=}")
    print(f"{sum(aset)/len(aset)=}")