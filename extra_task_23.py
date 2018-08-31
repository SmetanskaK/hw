from enum import IntEnum
import random
GREETING = '''
Enter data
0 - Rock
1 - Paper
2 - Scissors
(\'q\' for exit): '''


class Game(IntEnum):
    rock = 0
    paper = 1
    scissors = 2


def from_code2text(code):
    if code == Game.rock:
        return "ROCK"
    elif code == Game.paper:
        return "PAPER"
    elif code == Game.scissors:
        return "SCISSORS"


def who_is_winner(pc_choice, user_choice):
    if pc_choice == Game.rock and user_choice == Game.scissors:
        return False
    if pc_choice == Game.paper and user_choice == Game.rock:
        return False
    if pc_choice == Game.scissors and user_choice == Game.paper:
        return False
    return True


def game():
    while True:
        input_data = input(GREETING)
        if input_data == "q":
            break
        if not input_data.isnumeric():
            print("Invalid data!")
            continue

        if not Game.rock <= int(input_data) <= Game.scissors:
            print("Invalid data!")
            continue

        pc_choice = random.choice(list(Game))

        user_choice = Game(int(input_data))

        print("PC choice: %d" % pc_choice)
        if pc_choice == user_choice:
            print("Tie")
        else:
            if who_is_winner(pc_choice, user_choice):
                print("User is winner: %s vs %s" % (from_code2text(pc_choice),
                                                    (from_code2text(user_choice))))
            else:
                print("PC is winner: %s vs %s" %
                      (from_code2text(pc_choice),
                      (from_code2text(user_choice))))


game()
