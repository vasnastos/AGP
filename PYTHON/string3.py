value=input('Give Input Sequence:')

print('String Length:{}'.format(len(value)))

for key in value:
    print(f'{key}-->{ord(key)}')

value=value.replace(' ','')


showfrequency=dict()

for i in range(len(value)):
    if value[i] in showfrequency:
        showfrequency[value[i]]+=1
    else:
        showfrequency.update({value[i]:1})

print(showfrequency)