import random
import pandas

def guessing_game():
    number = random.randint(1,100)
    print("Welcome Player! In this game, you have to guess a number which is between 1 and 100")
    print("Good luck!")
    name = input("Enter your nickname: ")
    chance = 3
    while chance != 0:
        print(f"You have {chance}chance(s).")
        ask_number = input("Guess the number: ")
        ask_number = int(ask_number)
        if ask_number == number:
            print(f"You made it!{name}")
            break
        elif ask_number > number:
            print(f"Too high,{name}")
        elif ask_number < number:
            print(f"Too low,{name}")
        chance -= 1
    if chance == 0:
        print("You lose!")

def guess_base():
    bases = [2, 10, 16]
    base = random.sample(bases, 1)
    base = int(base[0])
    while True:
        ask_base = int(input("Guess the base: "))
        if ask_base == base:
            print("You made it")
            break
        elif base < ask_base:
            print("Too high")
        else:
            print("Too low")

def guess_word():
    with open('data.csv', 'r') as f:
        df = pandas.read_csv(f)
        starter = input('Input the start of the word you\'d like to guess: ')
        guess_wordw = ''.join(random.sample(list(df[starter.upper()]), 1))
        print(f'That word is {len(guess_wordw)} long.')
        count = 0
        while True:
            if count == 5:
                print(f'This its last three word!, {guess_wordw[-3:]}')
            guess = input(f'Guess the world which is start with {starter}: ')
            if guess == guess_wordw:
                print('EXcellent! You got it.')
                break
            print('You missed it.')
            count +=1
guess_word()