def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


numb = int(input("Enter your number:"))
if is_even(numb):
    print("Your number is even")
else:
    print("Your number is odd!")



