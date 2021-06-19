import requests as r
import statistics as s

codes=dict()
alldata=r.get('https://raw.githubusercontent.com/vasnastos/AGP/master/PYTHON/DATA/codes.csv').text
data=alldata.split('\n')
for k in data:
    if len(k.strip())==0: continue
    key,value=k.split(',')
    codes[key]=int(value)

#Sort a dictionary
def Sort(codes):
    return dict(sorted(codes.items(),key=lambda elem:elem[1]))

print(Sort(codes))
