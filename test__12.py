import random


def summer_test():
    lst_dup = []
    lst = []
    while len(lst) < 15:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        pair = str(a) + "*" + str(b)
        if pair not in lst_dup:
            lst.append(pair)
            lst_dup.append(pair)
            reversed_pair = str(b) + "*" + str(a)
            lst_dup.append(reversed_pair)

    return lst


print(summer_test())
