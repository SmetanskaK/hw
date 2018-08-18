def sum_of_digits(number):
    s = int(number[0]) + int(number[1]) + int(number[2])
    return s


number_1 = input("Enter your three-digit number:")
result = sum_of_digits(number_1)
print("Result is: %d" % result)
