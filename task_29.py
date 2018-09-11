import random


def gen_password():
    small_letters_underline_sym = "abcdefghijklmnopqrstuvwxyz_"
    numbers = "0123456789"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = small_letters_underline_sym + numbers + capital_letters
    box = ''
    random_index_1 = random.randint(0, len(small_letters_underline_sym) - 1)
    random_index_2 = random.randint(0, len(numbers) - 1)
    random_index_3 = random.randint(0, len(capital_letters) - 1)
    box = box + small_letters_underline_sym[random_index_1] + numbers[random_index_2] + capital_letters[random_index_3]
    for i in range(5):
        random_index = random.randint(0, len(result)-1)
        box = box + result[random_index]
    list_for_password = list(box)
    random.shuffle(list_for_password)
    r = ''.join(list_for_password)
    return r


print("Your password is", gen_password())
