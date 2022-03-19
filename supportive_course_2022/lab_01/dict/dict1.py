import sys
def exercise_1():
    # Write a Python script to add a key to a dictionary.
    # Sample Dictionary : {0: 10, 1: 20}
    # Expected Result : {0: 10, 1: 20, 2: 30}   
    numbers={
        0:10, 
        1:20
    }

    print("== Dictionary ==")
    print(numbers)
    x=int(input("Give input value:"))
    while x in numbers:
        print(f"Number {x} exists in dictionary!! Try again")
        x=int(input("Give input value:"))
    
    value=int(input(f"Give {x} value:"))
    numbers[x]=value
    print("== Dictionary ==")
    print(numbers)

def exercise_2():
    # Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

    # Sample Dictionary :
    # dic1={1:10, 2:20}
    # dic2={3:30, 4:40}
    # dic3={5:50,6:60}
    # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    numbers={
        1:10,
        2:20
    }

    numbers1={
        3:30,
        4:40
    }

    numbers2={
        5:50,
        6:60
    }

    numbers.update(numbers1)
    numbers.update(numbers2)
    print(numbers)

if __name__=='__main__':
    exp_id=int(sys.argv[1])
    if exp_id==1:
        exercise_1()
    elif exp_id==2:
        exercise_2()