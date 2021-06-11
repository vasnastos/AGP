mylist=[1,2,3,4,56,6,7,8,9,12,1,34,6,7,8]
shallowlist=mylist.copy()
deeplist=mylist
deeplist[5]=19
print(mylist,deeplist,end='\n\n')
shallowlist[5]=21
print(mylist,shallowlist,end='\n\n')

"""
    [1, 2, 3, 4, 56, 19, 7, 8, 9, 12, 1, 34, 6, 7, 8] [1, 2, 3, 4, 56, 19, 7, 8, 9, 12, 1, 34, 6, 7, 8]

    [1, 2, 3, 4, 56, 19, 7, 8, 9, 12, 1, 34, 6, 7, 8] [1, 2, 3, 4, 56, 21, 7, 8, 9, 12, 1, 34, 6, 7, 8]


"""