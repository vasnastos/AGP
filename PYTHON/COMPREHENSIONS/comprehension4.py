#List Comprehension which finds all prime numbers
def IsPrime(number):
    if number==1 or number==2:
        return True
    
    counter=2
    for i in range(2,number):
        if number%i==0:
            counter+=1
    
    return counter==2

def main():
    import random
    import time
    random.seed(time.time()*1000)
    #Fill list with a comprehension

    # Find using comprehension all the prime numbers

    # Show them as a string

    # Etc [1,2,3,4,5,7,8]
    #Output='1 3 5 7'


if __name__=='__main__':
    main()