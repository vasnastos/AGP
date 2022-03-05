import math

def sm(num:int):
    s=0
    for i in range(num):
        s+=1/math.pow(2,i)
    return s
    # return sum([math.pow(2,i) for i in range(num)])


if __name__=='__main__':
    while True:
        value=input('Give value')
        if not value.isdigit():
            value=input('Give value')
        if int(value)<=0:
            value=input('Give value')
        break
    print(sm(int(value)))