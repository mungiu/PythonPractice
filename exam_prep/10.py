# ex 11.1
numLst = [1, 2, 3, 4, 5]


def my_list_sum(myList):
    if len(myList) == 0:
        return 0
    else:
        return myList[0] + my_list_sum(myList[1:])
        # my_list[1:] is equivalent to a shallow copied list of all
        # elements starting from the 0-indexed 1


print(my_list_sum(numLst))

numLst = [1, 2, 3, 4, 5]
# using lambda
# expression_if_true if condition else expression_if_false
my_list_sum_lambda = lambda my_list: my_list[0] + my_list_sum_lambda(my_list[1:]) if my_list else 0
print(my_list_sum_lambda(numLst))


# ex 11.2
def rec_factorial(n):
    if n == 1:
        return n
    else:
        return n * rec_factorial(n - 1)


print(rec_factorial(10))

sum_sqr_ints = lambda first, second: first ** 2 + second ** 2

print(sum_sqr_ints(2, 2))

# ex 11.3
natural_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_even_numbers(number_list):
    # expression_if_true if condition else expression_if_false
    result = filter(lambda item: (item % 2 == 0), number_list)
    for i in result:
        print(i)

print_even_numbers(natural_numbers)


