import os


data=list()
with open(os.path.join('..','DATA','book.txt'),'r') as F:
    for line in F:
        print(line.strip())
        data.append(line.strip())

with open(os.path.join('..','DATA','export.txt'),'w') as FW:
    import datetime
    FW.write(datetime.datetime.now().strftime('%Y/%m/%d  %H:%M:%S'))
    FW.write('\n')
    FW.write('\n'.join(data))

with open(os.path.join('..','DATA','export.txt'),'a') as AW:
    import random
    AW.write('File opened at :')
    AW.write(datetime.datetime.now().strftime('%Y/%m/%d  %H:%M:%S'))
    AW.write('\n')
    AW.write('10 Random numbers\n')
    AW.write('**'*23+'\n')
    for _ in range(10):
        AW.write(str(random.randint(1,1000)))
        AW.write('\n')