import math
import random
lst = [random.randint(-1, 10) for i in range(10)]
print(lst)


def n(lst):
    max_num = lst[0]
    for i in range(len(lst)):
        if max_num < math.fabs(lst[i]):
            max_num = math.fabs(lst[i])
    for j in range(len(lst)):
        lst[j] = lst[j] / max_num
    return lst


print(n(lst))



