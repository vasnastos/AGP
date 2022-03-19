# immutability
a_dict = dict()

a_list = [1, 2]

# upcoming error
# a_dict[a_list] = 1

# convert to tuple
a_tuple = tuple(a_list)
a_dict[a_tuple] = 1

print(a_dict)

