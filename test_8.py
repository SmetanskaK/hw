import random
lst = [random.randint(0, 40) for i in range(10)]
print(lst)


def swap_max_and_min(lst):
    max_num_of_lst = max(lst)
    min_num_of_lst = min(lst)
    ind_of_max = lst.index(max_num_of_lst)
    ind_of_min = lst.index(min_num_of_lst)
    lst[ind_of_max], lst[ind_of_min] = lst[ind_of_min], lst[ind_of_max]
    return lst


print(swap_max_and_min(lst))
