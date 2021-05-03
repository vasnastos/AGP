#Write a Python program to separate and print the numbers and their 
#position of a given string.
import re

def ex_1():
    pattern='\d'
    stringgain='as23f45h67lk8912;l!34g7j90'
    counter=0
    for x in stringgain:
        if re.match(pattern,x):
            print(f'Str:{x}\tPos:{counter}')
        counter+=1

ex_1()