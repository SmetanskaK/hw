import random


def lst_1(num, lower_bound, upper_bound):
    list_of_nums = []
    for i in range(num):
        i = random.randint(lower_bound, upper_bound)
        list_of_nums.append(i)
    return list_of_nums


def calc_frequency(list_of_nums):
    a = list_of_nums.count(-1)
    b = list_of_nums.count(0)
    c = list_of_nums.count(1)
    if a == b or a == c or c == b:
        return None
    if a < b > c:
        return b
    if a < c > b:
        return c
    if c < a > b:
        return a


k = lst_1(11, -1, 1)
print(k)
print(calc_frequency(k))




