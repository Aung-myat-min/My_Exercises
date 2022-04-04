import random

def guessing_game():
    number = random.randint(1,100)
    print("Welcome Player! In this game, you have to guess a number which is between 1 and 100")
    print("Good luck!")
    name = input("Enter your nickname: ")
    while True:
        ask_number = input("Guess the number: ")
        ask_number = int(ask_number)
        if ask_number == number:
            print(f"You made it!{name}")
            break
        elif ask_number > number:
            print(f"Too high,{name}")
        elif ask_number < number:
            print(f"Too low,{name}")

guessing_game()