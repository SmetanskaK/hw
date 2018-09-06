import random

list_to_shuffle = [i for i in range(1, 100) if i % 2 != 0]
print(list_to_shuffle)


def shuffle_list(list_to_shuffle):
    for i in range(len(list_to_shuffle)):
        rand_index = random.randint(0, len(list_to_shuffle) - 1)
        temp = list_to_shuffle[i]
        list_to_shuffle[i] = list_to_shuffle[rand_index]
        list_to_shuffle[rand_index] = temp
    return list_to_shuffle


print(shuffle_list(list_to_shuffle))

