#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
import sys
if __name__=='__main__':
    args=sys.argv
    if len(args)!=2:
        print('Wrong amount of arguments')
        sys.exit(-1)

    number_of_samples=int(sys.argv[1])
    print(f"{number_of_samples=}")

    a_dict={x:x**2 for x in range(1,number_of_samples+1)}
    print(a_dict)

    for x in [12,2,7,4,9]:
        if x in args.items():
            print(f"key={x}  value:{args[x]}")
        else:
            print(f"Key {x} does not exist in dictionary")