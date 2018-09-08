import random


def lst_1(num, lower_bound, upper_bound):
    list_of_nums = [random.randint(lower_bound, upper_bound) for _ in range(num)]
    return list_of_nums


def calc_frequency(list_of_nums):
    a = list_of_nums.count(-1)
    b = list_of_nums.count(0)
    c = list_of_nums.count(1)
    if a == b or a == c or c == b:
        return None
    if a < b > c:
        return 0
    if a < c > b:
        return 1
    if c < a > b:
        return -1


k = lst_1(11, -1, 1)
print(k)
print(calc_frequency(k))




