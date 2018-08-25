import random


def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_of_even = 0
    sum_of_odd = 0
    for dummy in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number % 2 == 0:
            sum_of_even = sum_of_even + number
            print("Even!", sum_of_even)
        else:
            sum_of_odd = sum_of_odd + number
            print("Uneven!", sum_of_odd)

    return sum_of_even - sum_of_odd


print(diff_even_odd(5, 10, 15))
print(diff_even_odd(4, 0, 11))
