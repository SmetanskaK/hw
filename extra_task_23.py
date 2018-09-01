from enum import IntEnum
import random
GREETING = '''
Enter data
1 - Rock
2 - Paper
3 - Scissors
(\'q\' for exit): '''


Game = IntEnum('Game', 'ROCK PAPER SCISSORS')


def who_is_winner(pc_choice, user_choice):
    if pc_choice == Game.ROCK and user_choice == Game.SCISSORS:
        return False
    if pc_choice == Game.PAPER and user_choice == Game.ROCK:
        return False
    if pc_choice == Game.SCISSORS and user_choice == Game.PAPER:
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

        if not Game.ROCK <= int(input_data) <= Game.SCISSORS:
            print("Invalid data!")
            continue

        pc_choice = random.choice(list(Game))

        user_choice = Game(int(input_data))

        print("PC choice: %d" % pc_choice)
        if pc_choice == user_choice:
            print("Tie")
        else:
            if who_is_winner(pc_choice, user_choice):
                print("User is winner: %s vs %s" % (pc_choice, user_choice))
            else:
                print("PC is winner: %s vs %s" %
                      (pc_choice, user_choice))


game()
