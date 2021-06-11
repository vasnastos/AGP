mylist=['abc', 'xyz', 'aba', '1221']
counter=0
for x in mylist:
    if len(x)>2 and x[0]==x[len(x)-1]:
        counter+=1
print(counter)

# print(len([x for x in mylist if len(x)>2 and x[0]==x[len(x)-1]]))