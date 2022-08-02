# Simple Number Guesser Game using Python
import random

attempts_list = []


def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!\n")
    else:
        print(f"The current high score is {min(attempts_list)} attempts\n")


def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello! Welcome!\n")
    player_name = input("What is your name? \n")
    wanna_play = input(f"Hi, {player_name}, would you like to play the number guesser? \n(Enter Yes/No) \n")
    attempts = 0
    if wanna_play.lower() == "no":
        print("Okay never mind. Bye!")
        exit()
    elif wanna_play.lower() == "yes":
        show_score()
        while wanna_play.lower() == "yes":
            try:
                guess = input("Pick a number between 1 and 10 \n")
                if int(guess) < 1 or int(guess) > 10:
                    raise ValueError("Please guess a number within the given range")
                if int(guess) == random_number:
                    print("Yay!! You got it!\n")
                    attempts += 1
                    attempts_list.append(attempts)
                    print(f"It took you {attempts} attempts \n")
                    play_again = input("Would you like to play again?\n(Enter Yes/No)\n")
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 10))
                    if play_again.lower() == "no":
                        print("That's cool! Bye! \n")
                        break
                elif int(guess) > random_number:
                    print("It's lower.\n")
                    attempts += 1
                elif int(guess) < random_number:
                    print("It's higher.\n")
                    attempts += 1

            except ValueError as err:
                print("Oh no!That is not a valid value. Try again... \n")
                print(f"({err})\n")

            else:
                print("That's cool.\n")
    else:
        print("I don't understand. Wrong input.")
        exit()


if __name__ == '__main__':
    start_game()
