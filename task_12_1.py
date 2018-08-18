def sum_of_digits_1(number):
    a1 = number % 10
    a2 = (number % 100) / 10
    a3 = number / 100
    result = a1 + a2 + a3
    return result


number_2 = int(input("Enter your three-digit number:"))
result_1 = sum_of_digits_1(number_2)
print("Result is: %d " % result_1)
