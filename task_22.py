import random


def pc_code():
    code = random.randint(1, 11)
    return code


def game():
    a = pc_code()
    while True:
        num = input("Hello! Please enter your number: ")
        if num == "q":
            break
        if not num.isnumeric():
            print("Invalid data!")
            continue
        elif 1 > int(num) > 10:
            print("Invalid data!")
            continue
        if int(num) > a:
            print("Your num is bigger than mine!")
        elif int(num) < a:
            print("Your num is littler than mine!")
        else:
            print("You guess!")
            break


game()





