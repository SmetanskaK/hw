import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    max_num = lower_bound
    min_num = upper_bound
    for i in range(num_limit):
        v = random.randint(lower_bound, upper_bound)
        if v > max_num:
            max_num = v
        if v < min_num:
            min_num = v
    return max_num - min_num


print(diff_min_max(2, 1, 11))
print(diff_min_max(3, 0, 5))
