mylist1=[1,2,3,4,5,6,6,7,8,9,12,34,56]
mylist2=[1,2,89,19,4,65,45,13,9,12,34,56]

print(list(set(mylist1).difference(set(mylist2))))

# Comprehension Solution
print([x for x in mylist1 if x not in mylist2])

# for solution
"""
  container=list()
  for x in mylist1:
      if x not in mylist2:
          container.append(x)
  print(container)
"""