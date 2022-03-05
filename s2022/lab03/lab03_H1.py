import random
from statistics import mean
from time import time

def sum_test():
    random.seed(time())
    s=[]
    while sum(s)<1:
        s.append(random.uniform(0,1))
    print(mean(s))

if __name__ == '__main__':
    sum_test()
    