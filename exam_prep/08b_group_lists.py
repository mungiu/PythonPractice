num_lst = [1, 2, 3, 4, 5]


def sum_list(my_list):
    my_sum = 0
    for item in my_list:
        my_sum += item
    return my_sum


print(f"Sum of list is: {sum_list(num_lst)}")

num_lst = [1, 2, 3, 4, 5]


def group_list(my_list: list, g_length: int):
    outer_list = []
    inner_list = []
    count_outer_list: int = 0
    count_inner_list: int = 0
    while count_outer_list < len(my_list):
        if count_inner_list < g_length:
            list.append(inner_list, my_list[count_outer_list])
            count_inner_list += 1
            count_outer_list += 1
            if count_outer_list == len(my_list):
                list.append(outer_list, inner_list)
        else:
            list.append(outer_list, inner_list)
            count_inner_list = 0
            inner_list = []
    return outer_list


print(f"{group_list(num_lst, 2)}")

specialle = dict([
    ("Bob Builder", "IoT"),
    ("Dora Explorer", "Interactive Media"),
    ("Paw Patrol", "Data Engineering")
])
specialle["Bob Builder"] = "Data Engineering"
specialle["Farmer Pickles"] = "Climate Engineering"
print(specialle["Dora Explorer"])
print(specialle)
