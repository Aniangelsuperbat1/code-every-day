# Given a non-negative integer, return an array / a list of the individual digits in order.

# Examples:

# 123 => [1,2,3]

# 1 => [1]

# 8675309 => [8,6,7,5,3,0,9]

def digitize(n):
    new_array = []
    new_string = str(n)
    second_list = list(new_string)
    for num in second_list:
        new_num = int(num)
        new_array.append(new_num)
    return new_array