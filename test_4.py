def odd_product(number):
    number = str(number)
    box = 1
    for i in range(0, 5):
        if int(number[i]) % 2 != 0:
            box = box * int(number[i])
    return box


h = input("Enter your 5-digit num: ")
print("The result is %d" % odd_product(h))

