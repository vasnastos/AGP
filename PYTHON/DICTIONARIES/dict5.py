# Χρήση λεξικών στις εργασίες
#RPS RANDOM CHOICE
rps={0:'R',1:'P',2:'S'}
import random as r
from time import time
r.seed(time()*1000)
print('Random Move:{}'.format(rps[r.randint(0,2)]),end='\n\n')


#ΧΑΡΑΚΤΗΡΕΣ ΨΗΦΙΑ ΣΥΜΒΟΛΑ-dict --> str
stng="""
Copyright 2021 Nastos VASILEIOS!!!
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished_()# to do s#, subject t0 the following-
conditions:
The above copyright notice and this permission notice shall be included in !!all!! copies or substantial portions of the Software.
THE SOFTWARE!!!!!!~~ IS PROVIDED "AS IS"|||%^&&, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE!!@!!@.
"""
parser={'D':0,'L':0,'S':0}
for i in stng:
    if i.isdigit():
        parser['D']+=1
    elif i.isalpha():
        parser['L']+=1
    else:
        parser['S']+=1

from functools import reduce
print(reduce(lambda y,elem:y+f'{elem[0]}:{elem[1]}\n',parser.items(),''))