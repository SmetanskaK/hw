def find_closest(num_1, num_2):
    if abs(10 - num_1) > abs(10 - num_2):
        print("The second number is closer to 10!")
        return num_2
    elif abs(10 - num_1) < abs(10 - num_2):
        print("The first number is closer to 10!")
        return num_1
    else:
        print("Both numbers are equally close to 10!")
        return num_1, num_2


s = float(input("Enter the first num: "))
v = float(input("Enter the second num: "))
print(find_closest(s, v))