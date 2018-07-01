# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.


def sum_list(p):
    s = 0
    for e in p:
        s += e
    return s






print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134