import random


def get_max_digit(number):
    max = 0
    for i in range(0, 12):
        a = int((number % 10 ** (i + 1)) / (10 ** i))
        print(a)
        if a > max:
            max = a
    return max


j = random.randint(100000000000, 999999999999)
s = get_max_digit(j)
print(j)
print("Max digit of your num is: ", s)