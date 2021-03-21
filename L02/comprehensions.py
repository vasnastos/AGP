#[expression for item in iterable if condition == True]
list=['TOYOTA','NISSAN','FORD','FIAT']
k=[x for x in list if 'O' in x]
print(k)
l=[str(x)[::-1] for x in list]
print(l)

print(list[1:3])
print(list[::-2])
print(list[1:])
age=6
print('bigger' if age>5 else 'smaller')-->age>6?'bigger':'smaller'
sum(list)
