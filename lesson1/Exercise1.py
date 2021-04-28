import functools


# EX 8.1
def first_print():
    for count in range(10):
        print("PepePls")


def second_print():
    i = 0
    while i < 10:
        print("NotLikeThis")
        i += 1


def third_print(wish: object, qty):
    for count in range(qty):
        print(wish)


# def main():
#   first_print()
#   second_print()
#   third_print(input("input wish: "), int(input("input wish quantity: ")))


# EX 8.2 - SUM LIST (imperative VS declarative)
numbers = [1, 2, 3, 4, 5, 6]


# imperative programming – focuses on how to execute, defines control flow as
# statements that change a program state.
def sum_lst(lst):
    total = 0
    for number in lst:
        total += number
    return total


# declarative programming (functional) – focuses on what to execute, defines
# program logic, but not detailed control flow.
print(sum(numbers))  # using sum

print(functools.reduce(lambda x, y: x + y, numbers))  # using reduce


# EX 8.3 - check for even numbers (imperative VS declarative)
def print_even_input():
    temp = int(input())
    if temp % 2 == 0:
        print(temp)
    print_even_input()


# def main():
#   print_even_input()

# EX 8.4 - given a list and a group_length, returns a list of lists with length
# group_length.
def group_list(list, group_length):
    count = 1
    list_of_lists = []
    sub_list = []
    for item in list:
        sub_list.append(item)
        if count % group_length == 0:
            list_of_lists.append(sub_list.copy())
            sub_list = []
        count += 1
    return list_of_lists


# def main():
#   print(group_list(numbers, 2)) #[[1,2] [3,4] [5,6]]

# EX 8.5 - Create a dictionary specialle which stores software engineering
# specializations
dictionary_specialle = {"Bob": "IoT", "Dora": "Media", "Paw": "Data"}
dictionary_specialle["Bob"] = "Data"  # updating "Bob" value
dictionary_specialle.update({"Farmer": "Climate"})  # inserts new item to dictionary


def main():
    print(dictionary_specialle.get("Dora"))
    print(dictionary_specialle.keys())
    print(dictionary_specialle.get("Bob"))


main()
