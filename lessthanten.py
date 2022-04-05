a = [1,1,2,3,5,8,13,21,34,55,89]

# this block prints the numbers less than 5 one at a time as they are found.

# for i in a:
#     if i < 5:
#         print(i)
#     else:
#         continue


# this block makes a new list of the numbers that are less than 5 and prints the list

# less = list()
# for i in a :
#     if i < 5:
#         less.append(i)
#     else:
#         continue
# print(less)

# this block is the above code, but as a single line of syntax
# less = [i for i in a if i < 5]
# print(less)

# this block asks the user for a number and returns a list that contains only elements from a that are smaller than the given number.
num = int(input('Enter a number to query: '))
less = [i for i in a if i < num]
if len(less) > 0:
    print(less)
else:
    print('No numbers match your search.')