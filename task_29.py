import random


def gen_password():
    table = "abcdefghijklmnopqrstuvwxyz"
    table_1 = "0123456789"
    table_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table_3 = "_"
    result = table + table_1 + table_2 + table_3
    box = ''
    random_index_1 = random.randint(0, len(table) - 1)
    random_index_2 = random.randint(0, len(table_1) - 1)
    random_index_3 = random.randint(0, len(table_2) - 1)
    box = box + table[random_index_1] + table_1[random_index_2] + table_2[random_index_3]
    for i in range(5):
        random_index = random.randint(0, len(result)-1)
        box = box + result[random_index]
    list_for_password = list(box)
    random.shuffle(list_for_password)
    r = ''.join(list_for_password)
    return r


print(gen_password())
